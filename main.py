import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routes.api import router as api_router
from routes.webapp import web_router

app = FastAPI()

app.include_router(api_router, prefix="/api")
app.include_router(web_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
