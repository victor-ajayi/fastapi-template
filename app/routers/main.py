from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/ping")
def health_check():
    return {"status": "Healthy!"}
