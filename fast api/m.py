
from fastapi import FastAPI  
from typing import Optional , List # these are some libraries 
from uuid import uuid4, UUID # this librari defferent type of ides which usefull to bifardate defeent object 
from pydantic import BaseModel
from enum import Enum 

app = FastAPI()


class Gender(str, Enum):
    male = "male"
    female = "female"
class Role (str , Enum):
        admin = "admin"
        use = "use"
        student = "student "
    
class user(BaseModel) :
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
