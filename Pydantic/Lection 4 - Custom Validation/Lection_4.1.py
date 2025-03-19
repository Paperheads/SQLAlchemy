from pydantic import BaseModel, Field, ValidationError
#Customizing Field Validators

class User(BaseModel):
    name: str
    age: int = Field(gt=31)

try:
    user = User(name = 'Alice', age = 30)
    print(user)
except ValidationError as e:
    print(e)



#Bellow our custom validator
from pydantic import field_validator

class User(BaseModel):
    name: str
    age: int = Field(gt=0)

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v < 18 or v % 2 != 0:
            raise ValueError("age must be at least 18 and even")
        return v

try:
    user = User(name = 'Alice', age = 21)
    print(user)
except ValidationError as e: #Value error, age must be at least 18 and even
    print(e)