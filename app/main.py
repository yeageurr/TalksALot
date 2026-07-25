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
      "title": title
    }
  )

@app.get("/signup")
def signup_page(request: Request):
  title = "Chat App — Sign Up"
  return templates.TemplateResponse(
    request=request,
    name="pages/register.html",
    context={
      "title": title,
    }
  )


@app.get("/login")
def login_page(request: Request):
  title = "Chat App — Login"
  return templates.TemplateResponse(
      request=request,
      name="pages/login.html",
      context={
        "title": title,
      }
  )

@app.post('/auth-signup')
async def authenticate_signup(request: Request):
  pass