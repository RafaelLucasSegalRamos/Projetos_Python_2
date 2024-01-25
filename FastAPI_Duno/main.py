from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from urllib.parse import urlencode, quote_plus

from starlette.middleware.sessions import SessionMiddleware

from pydantic_settings import BaseSettings, SettingsConfigDict

from Secrets import Key  # Neste arquivo possui informações confidenciais de conta, por isso não está no repositório

# Para as variaveis abaixo basta usar o seus dados do Auth0
domain = Key().DOMAIN
client_id = Key().CLIENT_ID
client_secret = Key().CLIENT_SECRET
secret_key = Key().SECRECT_CODE
audience = Key().AUDIENCE  # Mesmo sendo puxado de outro arquivo está é uma variavel vazia.

oauth = OAuth()
oauth.register(
    name="auth0",
    client_id=client_id,
    client_secret=client_secret,
    server_metadata_url=f"https://{domain}/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid profile email",
    },
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict()
    domain: str = domain
    client_id: str = client_id
    client_secret: str = client_secret


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.mount("/static", StaticFiles(directory="static"), name="static")
print()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/login")
async def login(request: Request):
    if not 'id_token' in request.session:
        return await oauth.auth0.authorize_redirect(
            request,
            redirect_uri=request.url_for("callback"),
            audience=audience)
    return RedirectResponse('/')


@app.get("/callback")
async def callback(request: Request):
    token = await oauth.auth0.authorize_access_token(request)
    print(token)
    request.session['access_token'] = token['access_token']
    request.session['id_token'] = token['id_token']
    request.session['userinfo'] = token['userinfo']
    return RedirectResponse('/profile')


@app.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(
        url=f"https://"
            f"{domain}"
            f"/v2/logout?"
            f"{urlencode(
                {
                    'returnTo': request.url_for('/'),
                    'client_id': client_id},
                quote_via=quote_plus
            )}"
    )
    request.session.clear()
    return response


@app.get("/profile")
def profile(request: Request):
    return templates.TemplateResponse(request=request, name="profile.html", context={
        "request": request,
        'userinfo': request.session['userinfo']

        }
    )


# Link do video: https://www.youtube.com/watch?v=DeVCIU1JERc&list=TLPQMjMwMTIwMjQl7T2VvcgrMg
