from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.auth import (
    UserRegister,
    Token
)

from app.models.user import User
from app.models.tenant import Tenant

from app.auth.hashing import (
    hash_password,
    verify_password
)

from app.auth.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    tenant = Tenant(
        name=user_data.company_name
    )

    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    user = User(
        tenant_id=tenant.id,
        email=user_data.email,
        password=hash_password(
            user_data.password
        )
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "tenant_id": tenant.id
    }


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.email == form_data.username
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "tenant_id": user.tenant_id,
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
