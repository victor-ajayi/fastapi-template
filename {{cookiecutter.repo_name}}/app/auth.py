from datetime import datetime, timedelta

from app import database, schemas
from app.config import settings
from app.exceptions import InvalidCredentials, UnvalidatedCredentials
from app.models import User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(payload: dict):
    payload.update(
        {"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    )
    encoded_jwt = jwt.encode(payload, SECRET_KEY, ALGORITHM)

    return encoded_jwt, ACCESS_TOKEN_EXPIRE_MINUTES


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id: int = payload.get("user_id")
        if not id:
            raise InvalidCredentials
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise InvalidCredentials

    return token_data["id"]


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)
) -> User | None:
    user_id = verify_access_token(token)

    return db.query(User).filter_by(id=user_id).first()
