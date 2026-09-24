from pydantic import BaseModel

# Define schema models for user registration
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"  # Default role is 'user'

# Define schema model for user login
class UserLogin(BaseModel):
    username: str
    password: str