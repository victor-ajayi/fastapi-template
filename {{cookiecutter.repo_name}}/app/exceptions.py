from fastapi import HTTPException, status

UnvalidatedCredentials = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Unable to verify credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)

InvalidCredentials = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)
