from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import engine
from engine import content_df
from engine2 import content_df as content_df2

app = FastAPI()

# Allow all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Call


# Call engine function (ie; engine/recommend/...)
@app.post("/engine/{function_name}")
async def call_function(function_name: str, request: Request):
    function_to_call = getattr(engine, function_name)
    body = await request.json()
    result = function_to_call(body)
    return result


# Given fruit, what is shortest path to get to fruit via flight
@app.post("/shortestPath")
async def shortestPath(request: Request):
    body = await request.json()


# Get random user
@app.get("/getUser")
async def getUser():
    # Random user function from engine.py
    return content_df["ID"].sample().values[0]


# Get random fruit
@app.get("/getFruit")
async def get_fruit(num: int = 1):
    fruits = content_df["Fruit"].sample(n=num).values.tolist()
    return fruits


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
