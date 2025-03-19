#Closer look at Error Objects



from pydantic import ValidationError, BaseModel, field_validator


#bassicaly validationError is subclass of Value Error
print(issubclass(ValidationError, ValueError)) #True
print(ValidationError.__mro__) #(<class 'pydantic_core._pydantic_core.ValidationError'>, <class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)



class User(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8 or not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least 8 characters and contain at least one digit")

        return v

#try:
#    user = User(username = "Andy", password = "abcabcabc")
#except ValidationError as e:
#    print(e)


#Make the exception more system friendly!

try:
    user = User(username = "Andy", password = "abcabcabc")
except ValidationError as e:
    #print(e.json(indent=2))
    #or we can get it as a dict
    #print(e.errors())
    #and work as with dict
    print(e.errors()[0]['type']) #value_error

'''
(<class 'pydantic_core._pydantic_core.ValidationError'>, <class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
[
  {
    "type": "value_error",
    "loc": [
      "password"
    ],
    "msg": "Value error, Password must contain at least 8 characters and contain at least one digit",
    "input": "abcabcabc",
    "ctx": {
      "error": "Password must contain at least 8 characters and contain at least one digit"
    },
    "url": "https://errors.pydantic.dev/2.10/v/value_error"
  }
]
'''