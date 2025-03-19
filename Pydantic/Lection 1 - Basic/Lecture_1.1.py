import pydantic

print(pydantic.VERSION)  # 2.10.6

from pydantic import BaseModel


# Here we define what we are going to catch(define models)
class User(BaseModel):
    name: str
    age: int
    email: str


user = User(name="John Doe", age=25, email="johndoe@gmail.com")

print(user)  # = name='John Doe' age=25 email='johndoe@gmail.com'

print(user.name)  # John Doe
print(user.age)  # 25
print(user.email)  # johndoe@gmail.com

# Alternative scenario
# user1 = User(name = "John Doe", age ='25asdsa', email = "johndoe@gmail.com") #We will have an error!

# Usually we put this into try-except statement

try:
    user1 = User(name="John Doe", age='25asdasd', email="johndoe@gmail.com")
except pydantic.ValidationError as e:
    print(e)

try:  # Here we are left only the digit in the age as a string!
    user1 = User(name="John Doe", age='25', email="johndoe@gmail.com")  # It will work!
except pydantic.ValidationError as e:
    print(e)

# Pydantic by default tries to convert data into right one. As int(age)


#Create config
class User(BaseModel):
    name: str
    age: int
    email: str

    class Config:
        strict = True

try:
    user1 = User(name="John Doe", age='25', email="johndoe@gmail.com")  # It will work!
except pydantic.ValidationError as e:
    print(e)

#Now we will raise an expection because we create a strict validation!
#But with this way we can't apply the setting to a some of the data, only for all of them

from pydantic import StrictInt

class User(BaseModel):
    name: str
    age: StrictInt #Now it is applied only for this part!
    email: str

try:
    user1 = User(name="John Doe", age='25', email="johndoe@gmail.com")  # It will work!
except pydantic.ValidationError as e:
    print(e)