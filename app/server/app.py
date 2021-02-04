from fastapi import FastAPI
from server.routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouterm tags=["Students"], prefix="/student")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}