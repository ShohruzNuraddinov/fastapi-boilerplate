from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base model for User.
    """
    username: str


class UserCreate(UserBase):
    """
    Model for creating a new user.
    """
    email: str = None
    hashed_password: str

class UserUpdate(UserBase):
    """
    Model for updating an existing user.
    """
    id: int
    email: str = None
    password: str = None


class UserLogin(UserBase):
    """
    Model for user login.
    """
    password: str