import uvicorn
from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def return_index():
    return {"message": "Hello index"}


@app.get("/hello/")
def hello_name(name: str = "Anon"):
    name = name.strip().title()
    return {"hello": f"Hello {name}!"}


@app.get("/items/")
def list_items():
    return {"Item1", "Item2", "Item3"}


@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": item_id,
    }


@app.post("/users/")
def create_user(user: CreateUser):
    return {"message": "success", "email": user.email}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
