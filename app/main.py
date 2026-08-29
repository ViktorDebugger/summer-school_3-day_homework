from fastapi import FastAPI

app = FastAPI(title="Summer School Day 3 Homework")


@app.get("/")
def read_root():
    return {"message": "Summer School Day 3 Homework API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/about")
def about():
    return {
        "project": "summer-school_3-day_homework",
        "description": "FastAPI homework project for the Git/GitHub summer school course",
    }


@app.get("/items")
def list_items():
    return {"items": ["git", "github", "fastapi", "pytest"]}
