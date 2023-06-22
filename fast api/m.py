# This file is created to help the main file in giving a request 
from fastapi import FastAPI  
from typing import Optional, List # these are some libraries 
from uuid import uuid4, UUID # this library different type of ideas which help to bifurcate different object 
from pydantic import BaseModel
from enum import Enum 

app = FastAPI() # I created a app(app method) using fastapi


class Gender(str, Enum):
    male = "male"
    female = "female"
class Role (str , Enum):
        admin = "admin"
        use = "use"
        student = "student "
    
class user(BaseModel) : # user is the subclass of base-model we can use base model properties in user class 
    id : Optional[UUID] = uuid4 
    first_name :str
    last_name : str
    middle_name : Optional[str]
    gender : Gender 
    roles : List[Role]
    

class userupdate(BaseModel):
    first_name = Optional[str]
    last_name = Optional[str]
    last_name = Optional [str]
    role = Optional[list[Role]]
