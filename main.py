#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#FastAPI

from fastapi import FastAPI
from fastapi import Body
from fastapi import Query, Path

app= FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_marriaged: Optional[bool] = None

class Location(BaseModel):
    country: str
    state:str
    city: str



@app.get('/')
def home():
    return{'Hello':'Wolrd'}


#rquest and rosponse body

@app.post('/person/new')

def create_funtion(persona: Person= Body(...)):
    return Person


#validations: query parameters

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None, min_length=1, 
        max_length=50,
        title='Person name',
        description= 'This is the person name. It is between 1 and 50 characters '
        ),
    age: str = Query(
        ...,
        title='Person age',
        drescription='This is the person age, this is required.'
    ) 
):
    return {name: age}
 
 # validaciones: path parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='Person Id',
        description='This is the person ID, it is important to identify each person.'
        )
 ):
    return {person_id: 'It exist!'}

    # validaciones: request body

@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        title='person ID',
        description='This is the person ID',
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...) # we can create another request body

):
    results = person.dict()
    results.update(location.dict())
    return results