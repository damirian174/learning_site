from pydantic import BaseModel

class SUser(BaseModel):
    name: str
    email: str

class STask(BaseModel):
    title: str
    description: str