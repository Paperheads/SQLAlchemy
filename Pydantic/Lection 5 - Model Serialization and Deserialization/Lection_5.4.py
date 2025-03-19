#Deserialization

from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: Optional[EmailStr] = None


user_data = ' {"name": "Alice", "age": 30, "email": "alice@example.com"} ' #This is as json

#With pydantic we can validate the incoming data

user = User.model_validate_json(user_data) #name='Alice' age=30 email='alice@example.com'
print(user.name) #Alice

#imagine we have a list of values, and we want to take only the right one!

users_data = [
    '{"name": "Alice", "age": 30, "email": "alice@hotmail.com"}',
    '{"name": "Bob", "age": "30", "email": "brian@gmail"}',
    '{"name": "Charlie", "age": 25, "email": "tiana"}'
]

for u in users_data:
    try:
        user = User.model_validate_json(u)
        print("VALID USER:")
        print(user, end = "\n\n")

    except ValidationError as e:
        print(e.errors()[0]["msg"])

"""
Output:
VALID USER:
name='Alice' age=30 email='alice@hotmail.com' 
value is not a valid email address: The part after the @-sign is not valid. It should have a period.
value is not a valid email address: An email address must have an @-sign.
"""