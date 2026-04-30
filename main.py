from fastapi import FastAPI
from api.api import api_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn



app = FastAPI(title="Commit Craft Application")
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
)

app.mount("/static",StaticFiles(
    directory="static"),
    name="static"
    )


@app.get('/')
def home():
    return FileResponse("static/index.html")


app.include_router(api_router,prefix="/api")





if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)

