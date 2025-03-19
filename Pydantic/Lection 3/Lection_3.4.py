#Additional Properties

from pydantic import BaseModel, Field, ValidationError
from uuid import UUID, uuid4

class Product(BaseModel):
    id: UUID = Field(frozen=True, default_factory=uuid4)
    name: str

try:
    #product = Product(name = "Chair")
    product = Product(name="Chair", price = 202) #Pydantic is okay with PRICE but it's strange!
    #Price is not in our model!! Pydantic just ignores it

    print(product)
except ValidationError as e:
    print(e)


#Let's change!

class Product(BaseModel):
    id: UUID = Field(frozen=True, default_factory=uuid4)
    name: str

    class Config:
        #extra = "ignore" - default
        extra = "forbid" #normaly it is in "ignore" - that mean just ignoring errors


try:
    product = Product(name="Chair", price=202)   #Extra inputs are not permitted
    #So now we have an error here!
    print(product)
except ValidationError as e:
    print(e)



class Product(BaseModel):
    id: UUID = Field(frozen=True, default_factory=uuid4)
    name: str

    class Config:
        #extra = "ignore"
        #extra = "forbid"
        extra = "allow"  #Allow changes!


try:
    product = Product(name="Chair", price=202, weight = 20.3)
    print(product) #id=UUID('fc9cd5a8-c20c-4a68-9d7e-7c616eebb9b2') name='Chair' price=202 weight=20.3
except ValidationError as e:
    print(e)