import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import router


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)
