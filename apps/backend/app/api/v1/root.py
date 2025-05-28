from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Health"])
def health_check():
    return {"message": "Guia de Bares SP API rodando 🍻"}