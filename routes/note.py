

# routes define all the connection setting for the app


from typing import Union
from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from models.note import Note
from schemas.note import noteEntity, notesEntity


note = APIRouter()
templates = Jinja2Templates(directory="templates")


# html template and mongo client response
# get method means we are fetching a note from the database
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notesDB.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


# post method means a new note will be created in the database
@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] == "on" else False
    conn.notesDB.notes.insert_one(formDict)
    return{"Success": True}



