from google import genai
from google.genai import types
from fastapi.responses import StreamingResponse
from core.config import MODE_NAME,TEMPERATURE
from core.llm import llm
from models.request_schema import RequestData
from services.prompts.commit_craft_prompt import prompt



def commit_create(data:RequestData):
    for chunk in llm.models.generate_content_stream(
    model=MODE_NAME,
    contents=[prompt.format(
        commit_type=data.commit_type,
        scope=data.scope,
        what_changed=data.what_did_you_change,
        breaking_change=data.breaking_change
    )]
):
        if chunk.text:
            yield chunk.text
            



def greet(data:RequestData):
    return StreamingResponse(
        commit_create(data),
        media_type="text/plain"
    )