from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# data model 
class Item(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

#Simulasi database
items_db = {}

#Root
@app.get("/")
def read_root():
    return {"message": "Hello World"}

#create (POST)
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in items_db:
        return {"error": "Item already exists"}

    items_db[item_id] = item.dict()
    return {
        "message": "Item created successfully",
        "item_id": items_db[item_id]
        }
#Read (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'item_id': item_id, 'item': items_db[item_id]}
#Update (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        return {"error": "Item not found"}
    
    items_db[item_id] = item.dict()
    return {
        "message": "Item updated successfully",
        "item_id": items_db[item_id]
    }
#Delete (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    
    delete_item=items_db.pop(item_id)
    return {
        "message": "Item deleted successfully",
        "item_id": item_id
    }        
    