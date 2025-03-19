# Immutable Attributes

'''
Immutable objects have several desirable characteristics:
• They contribute to data integrity: Immutable
attributes prevent accidental or unauthorized
modifications, ensuring the consistency of data.

• They are predictable: Having attributes that don't
change state after creation makes the behavior of your
models more predictable.

• Concurrency safety: In concurrent programming, immutable
objects are safer to use as they can't be modified after
creation, reducing the risk of data races.
'''

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    name: str
    age: int


try:
    user = User(name="Alice", age=30)
    print(user.name)  # Alice

    user.name = 'Billy'
    print(user.name)  # Billy
except ValidationError as e:
    print(e)


class User(BaseModel):
    name: str
    age: int

    class Config:
        frozen = True  # OLD WAY


try:
    user = User(name="Alice", age=30)
    print(user.name)  # Alice

    user.name = 'Billy'
    print(user.name)  # Instance is frozen [type=frozen_instance, input_value='Billy', input_type=str]
except ValidationError as e:
    print(e)

# new way
from pydantic import ConfigDict


class User(BaseModel):
    model_config: ConfigDict = {"frozen": True}

    name: str
    age: int

try:
    user = User(name="Alice", age=30)
    print(user.name)  # Alice

    user.name = 'Billy'
    print(user.name)  # Instance is frozen [type=frozen_instance, input_value='Billy', input_type=str]
except ValidationError as e:
    print(e)


#Make some attribute acceptable to mutable
from pydantic import Field

class User(BaseModel):

    id : int = Field(frozen=True)
    name: str
    age: int

try:
    user = User(id = 123, name="Alice", age=30)
    print(user.id, user.name)
    user.name = 'Billy' #okay here
    user.id = 10 #Mistake here

except ValidationError as e:
    print(e)