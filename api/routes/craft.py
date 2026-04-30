from fastapi import APIRouter
from services.commit import greet
from models.request_schema import RequestData
router = APIRouter()

@router.post("")
def upload_deatils(data:RequestData):
    return greet(data)
