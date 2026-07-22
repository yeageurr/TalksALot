#from app.db_config import generate_tables
from jinja2.ext import loopcontrols

from fastapi import FastAPI, WebSocket, Request, Query, status, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="ChitChat")
app.mount("/static", StaticFiles(directory="app/static"), "static")
templates = Jinja2Templates(directory="app/templates")
templates.env.add_extension(loopcontrols)

app.add_middleware(
  CORSMiddleware,
  allow_origins="*",
  allow_credentials=True,
  allow_methods="*",
  allow_headers="*"
)

@app.get("/")
def index_page(request: Request):
  title = "Chat App"
  return templates.TemplateResponse(
    request = request,
    name = "index.html",
    context = {
      "request": request,
      "title": title
    }
  )
