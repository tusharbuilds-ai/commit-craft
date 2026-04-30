from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()

@router.get("")
def home():
    return FileResponse("static/index.html",
                        headers={
                            "Cache-Control":"no-store,no-cache,must-revalidate",
                            "Pragma":"no-cache"
                        })
