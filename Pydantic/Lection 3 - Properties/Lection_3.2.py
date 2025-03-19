# UUIDs and Default Factories

# UUID -> universally unique identifiers
# GUID -> globally unique identifiers

# e.g.da3a3ea3-1b95-4b35-ad10-3ac541d4bde7

from pydantic import BaseModel, ValidationError

# out uuid
import uuid

print(uuid.uuid4())  # 7d0312e2-262f-4550-9f74-69cf4cf24a8f and every time different one!


# The UUID are used in many application as a generating unique id, creating session token
# securing API's etc

class User(BaseModel):
    id: uuid.UUID
    name: str


try:
    user = User(id=uuid.uuid4(), name="Allison")
    print(user)  # id=UUID('2d6d34bb-edd6-4729-9cd7-017cb626c0df') name='Allison'
    # user = User(id = 'asdasdsadasd', name = "Allison") #Error! Input should be a valid UUID
except ValidationError as e:
    print(e)

# Default factory

from pydantic import Field


class User(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    name: str


user_2 = User(name="Davyd") #id=UUID('0b43a848-ddb0-465f-92b2-1ba1a7ff1c9c') name='Davyd'
print(user_2)



#Even More elegant way

class User(BaseModel):
    id: uuid.UUID = Field(default_factory= uuid.uuid4)
    name: str

user_2 = User(name="Davyd") #work
print(user_2)


#We also can add the uuid by our own. But it's not necessary
