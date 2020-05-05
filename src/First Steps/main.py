from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World!"}

@app.get("/fruits-list/")
def fruit_list():
    return ['Apple', 'Mango', 'Grapes']

@app.get("/fruit/{item_id}")
def read_fruit(item_id):
    fruits = ['Apple', 'Mango', 'Grapes']
    return fruits[int(item_id)]

@app.get("/fruit_v2/{id}")
async def read_fruit(id:int):
    fruits = ['Apple','Mango','Grapes']
    return fruits[id]

@app.get('/greeting')
async def personal_greeting(name:str = "John Doe"):
    return {"message":"Hi "+name}

class User(BaseModel):
    email: str
    password: str

@app.post("/login")
async def login(user: User):
    return user.email + " has successfully logged in with password: " + user.password