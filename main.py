from fastapi import FastAPI, Query

app = FastAPI(
    title="Hello Business",
    version="1.0.0",
)

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