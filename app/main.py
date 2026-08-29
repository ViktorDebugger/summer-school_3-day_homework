from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Summer School Day 3 Homework")


class Item(BaseModel):
    name: str


items_db: dict[int, str] = {}
next_item_id = 1


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
    return {"items": items_db}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_item_id
    item_id = next_item_id
    items_db[item_id] = item.name
    next_item_id += 1
    return {"id": item_id, "name": item.name}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": items_db[item_id]}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
