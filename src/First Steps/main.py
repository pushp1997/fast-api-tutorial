from fastapi import FastAPI

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