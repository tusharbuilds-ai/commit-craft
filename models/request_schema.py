from pydantic import BaseModel

class RequestData(BaseModel):
    commit_type:str
    what_did_you_change:str
    scope:str 
    breaking_change: str