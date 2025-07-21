from fastapi import FastAPI #Python backend framework which collects data from UI
from pydantic import BaseModel #Pydantic verifies and parses the received input; We can avoid try/except logic using Pydantic
from generator import generate_story #We are importing the generate_story function from the already written 'generator.py' code

app = FastAPI() #Initialising FASTAPI app; app is an object of FASTAPI class which does all the communications

#Defining the request body schema
class PromptRequest(BaseModel): #Creating a local class which inherits all the charactors of 'BaseModel' class from pydantic library
    prompt: str                 #Tells python that a 'prompt' variable with string type is passed; 
    
#Define the POST endpoint
@app.post("/generate") #A decorator which creates a route URL at /generate that listens for POST requests
#We are posting the data obtained from /generate url to server
def generate(req: PromptRequest):
    story = generate_story(req.prompt) #Calls the GPT2 generator
    return {"story": story} #Returns a JSON with the generated story






