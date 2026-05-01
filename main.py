from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router
import uvicorn

app = FastAPI(title="Commit Craft Application")

@app.middleware("http")
async def force_https(request: Request, call_next):
    proto = request.headers.get("x-forwarded-proto", "https")
    if proto == "http":
        url = str(request.url).replace("http://", "https://", 1)
        return RedirectResponse(url, status_code=308)
    return await call_next(request)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get('/')
def home():
    return FileResponse("static/index.html")

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)