from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models.product import Product
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI(
    title="Hello Business",
    version="1.0.0",
)


Base.metadata.create_all(bind=engine)

AUTHOR = "Igor Drohomirecki"
FRAMEWORK = "FastAPI"

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
@app.get("/api/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products