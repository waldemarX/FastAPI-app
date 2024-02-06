from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/chat")
def get_chat_page(request: Request):
    return templates.TemplateResponse(
        "chat.html", context={"request": request}
    )
