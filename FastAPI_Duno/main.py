from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from Secrets import Key  # Neste arquivo possui informações confidenciais de conta, por isso não está no repositório

# Para as variaveis abaixo basta usar o seus dados do Auth0
domain = Key().domain
client_id = Key().client_id
client_secret = Key().client_secret

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")

# Link do video: https://www.youtube.com/watch?v=DeVCIU1JERc&list=TLPQMjMwMTIwMjQl7T2VvcgrMg
