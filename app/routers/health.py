from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "FlyRank Widget Platform"
    }


@router.get("/ready")
def readiness_check():
    return {
        "status": "ready"
    }