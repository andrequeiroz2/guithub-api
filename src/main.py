import uvicorn
from fastapi import FastAPI
from config.config import settings
from endpoint.github import github_router

app = FastAPI()

app.include_router(github_router, tags=["Repository"])

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, log_level=settings.LOG_LEVEL)


