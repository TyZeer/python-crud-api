from pydantic import BaseModel, EmailStr, Field
from annotated_types import Annotated, MaxLen, MinLen


class CreateUser(BaseModel):
    username: str = Field(..., min_length=5, max_length=100)
    passphrase: Annotated[str, MinLen(10), MaxLen(20)]
    email: EmailStr
