#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#FastAPI

from fastapi import FastAPI
from fastapi import Body

app= FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_marriaged: Optional[bool] = None


@app.get('/')
def home():
    return{'Hello':'Wolrd'}


#rquest and rosponse body

@app.post('/person/new')

def create_funtion(persona: Person= Body(...)):
    return Person
    
