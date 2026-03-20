from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models.product import Product

app = FastAPI(
    title="Hello Business",
    version="1.0.0",
)

AUTHOR = "Igor Drohomirecki"
FRAMEWORK = "FastAPI"

MODELS = {
    "products": Product,
}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.get("/hello")
def hello():
    return "Hello, World!"

@app.get("/hello/{name}")
def hello_name(name: str):
    return f"Hello, {name}!"

@app.get("/greet")
def greet(name: str = Query(..., description="Imię do przywitania")):
    return f"Hello, {name}!"

@app.get("/info")
def info():
    return {
        "autor": AUTHOR,
        "framework": FRAMEWORK,
        "wersja_aplikacji": app.version,
    }

@app.get("/api/{encja}")
def get_all_records(encja: str, db: Session = Depends(get_db)):
    model = MODELS.get(encja)

    if not model:
        raise HTTPException(status_code=404, detail="Encja nie istnieje")

    records = db.query(model).all()
    return records
@app.get("/api/{encja}/{id}")
def get_record_by_id(encja: str, id: int, db: Session = Depends(get_db)):
    model = MODELS.get(encja)

    if not model:
        raise HTTPException(status_code=404, detail="Encja nie istnieje")

    record = db.query(model).filter(model.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Rekord nie istnieje")

    return record