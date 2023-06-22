from fastapi import FastAPI ,HTTPException
import random
from uuid import uuid4 , UUID
from typing import List 
from m import user , Gender , Role

app = FastAPI()

#  /// get request 

# @app.get("/") # this is the basic mathod to create an web page 
#                 # this calls the get requist to create a web page 
#                 # if you want to manege the http link you can use attributes og this requrst 
# def root(): # this is the user define function
#         #   it handels a ge request to the root path and return jsson reponce 
#     return {"hello" :"onkar"} #this is the basic 

# @app.get("/items")
# def read(q: str = None):
#     if q:
#         return {"message": f"Items with query '{q}'"}
#     return {"message": "Items"}

# # ------------------put request()--------------------

# @app.post("/items")
# def create_item():
    # Code to handle the POST request for /items
    # ...
    
    
# If you are using third party libraries that
# tell you to call them with await
# Then, declare your path operation functions with async def
'''If you are using a third party library that communicates 
# with something (a database, an API, the file system, etc.)
# and doesn't have support for using await'''
# you can use await only inside async def function 


# syncronous work - you have wait for some time when third parti is doing their work 
# asyncronous work  - you don't have to wait at that time when third parti is doing their work 
# you do deffernt work at that time not mouch productive 

db : List[user] = [user(id  = uuid4 (), # i created a database which cantins different tuype of atribute 
        first_name = "onkar",# and i used sone other file to criating it which i made before 
        last_name = "raput ",
        gender = Gender.male,
        roles = [Role.student])]
@app.get("/") # this is the basic mathod to create an web page 
#                 # this calls the get requist to create a web page 
#                 # if you want to manege the http link you can use attributes og this requrst 
def root(): # this is the user define function
#         #   it handels a ge request to the root path and return jsson reponce 
 return {"hello" :"onkar"} #this is the basic
@app.get("/api/v1/user")# you can handle HTTP link by passing the text in the get function 
def fetch():
    return db 
@app.post("/api/v1/user") # this is the post methoed to add thingd in datsbase 
def resiter(user : user):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/user/{user_id}") # this the the delete method to delete the object from the data base
def deleteuser(user_id : UUID):
    for user in db :
        if user.id == user_id :
            db.remove(user)
        return 
   
    raise HTTPException(  # it gives an arror if there is no request can apply for apsific user 
        status_code = 404, 
        detail = f"user with id: {user_id} does not exist"
        )