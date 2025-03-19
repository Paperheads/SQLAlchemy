#Type, Hinting, Foundations
#Optional, Any and Defaults

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int


try:
    user1 = User(name = "Alice")
    print(user1.age)
except ValidationError as e: #1 validation error for User
    print(e)


#BUT!

from pydantic import BaseModel, ValidationError
from typing import Optional

class User(BaseModel):
    name: str
    age: Optional[int] = None


try:
    user1 = User(name = "Alice")
    print(user1.age) #None
except ValidationError as e:
    print(e) #The exception won't be raised

print(user1) #name='Alice' age=None


#Additional information

#if you want a value to not be required at
#instantiation set a default alongside a type annotation,
# e.g. age: int = 33

#if, in addition to not being required, you want
# the field to be nullable, meaning possibly assume
# the value of None, then all you need to do is wrap
# the type in Optional, e.g. age: Optional[int] = 33

#• if, in addition to nullable and not being required,
# you also want the field to not be type checked,
# then you use Any instead of the
#type, alongside a specified default, e.g. age: Any = 33


from typing import Any
#Demostration
class Mnemonic(BaseModel):
    requiredIntQuantity: int
    optionalIntQuantity: int = 10
    optionalIntQuantityNullable: Optional[int] = 10
    optionalAnyTypeQuantity: Any = 10
