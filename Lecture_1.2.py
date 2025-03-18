import pydantic
from pydantic import StrictInt, BaseModel

class User(BaseModel):
    name: str
    age: StrictInt #Now it is applied only for this part!
    email: str

try:
    user1 = User(name="John Doe", age='25', email="johndoe@gmail.com")  # It will work!
except pydantic.ValidationError as e:
    print(e)


#We want to apply additional conditions
#1 age should be between 18 and 120 years old
#2 name should be between 3 and 50 characters long
#3 email should be a valid email address

from pydantic import Field, EmailStr
class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: StrictInt = Field(gt=18, lt=120) #greater than and less than
    email: EmailStr

#To use emailstr we have to install additional package -> pip install email-validator

try:
    user1 = User(name="sdJo", age= 20, email="johndoe@gmail.com")  # It will work!
except pydantic.ValidationError as e:
    print(e)
#The age should be greater than 18 - mistake!
#The name should have at least 3 characters
#An email address must have an @-sign