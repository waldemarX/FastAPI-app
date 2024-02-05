"""Base responses"""


from fastapi import HTTPException


def response_ok(data, detail=None):
    return {
        "status": "success",
        "data": data,
        "detail": detail
    }


def response_error():
    raise HTTPException(
            status_code=500,
            detail={"status": "error", "data": None, "detail": None},
        )
