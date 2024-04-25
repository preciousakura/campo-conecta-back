from fastapi import APIRouter

router = APIRouter(
  prefix="/auth",
  tags=["auth"]
)

@router.get("/")
def test_route():
  return { "message": "Hello world" }