from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import settings
from app.database import Base, engine

# ==========================
# Import Models
# ==========================
from app.models.user import User
from app.models.tenant import Tenant
from app.models.widget import Widget
from app.models.submission import Submission

# ==========================
# Routers
# ==========================
from app.routers.auth import router as auth_router
from app.routers.widgets import router as widgets_router
from app.routers.public import router as public_router
from app.routers.dashboard import router as dashboard_router
from app.routers.health import router as health_router

# ==========================
# Middleware
# ==========================
from app.middleware.cors import add_cors
from app.middleware.logging import log_requests

# ==========================
# Rate Limiter
# ==========================
from app.services.rate_limit import (
    limiter,
    rate_limit_exception,
    rate_limit_handler,
)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="FlyRank Embeddable Widget & Lead Capture Platform",
)

Base.metadata.create_all(bind=engine)

app.state.limiter = limiter

app.add_exception_handler(
    rate_limit_exception,
    rate_limit_handler,
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# Middleware
add_cors(app)
app.middleware("http")(log_requests)

# Routers
app.include_router(auth_router)
app.include_router(widgets_router)
app.include_router(public_router)
app.include_router(dashboard_router)
app.include_router(health_router)


@app.get("/", tags=["Home"])
def root():
    return {
        "message": "Welcome to FlyRank Embeddable Widget Platform",
        "version": "1.0.0",
        "status": "running",
    }


# ====================================================
# Versioned Widget Script
# ====================================================

@app.get("/widget.js")
def widget_js():
    response = FileResponse(
        "app/static/widget.js",
        media_type="application/javascript",
    )

    response.headers["Cache-Control"] = (
        "public, max-age=31536000, immutable"
    )

    return response
