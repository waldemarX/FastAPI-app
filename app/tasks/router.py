from fastapi import APIRouter, Depends

from auth.config import current_user
from .tasks import send_email_random_cat
from base_responses import response_ok


router = APIRouter()


@router.get("/cat_mail")
def get_cat_mail(user=Depends(current_user)):
    send_email_random_cat.delay(user.username)
    return response_ok(data="Email sent!")
