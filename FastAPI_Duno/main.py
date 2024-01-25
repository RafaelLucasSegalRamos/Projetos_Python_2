from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from urllib.parse import urlencode, quote_plus

from starlette.middleware.sessions import SessionMiddleware

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )
    DOMAIN: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    SECRET_KEY: str
    AUDIENCE: str


settings = Settings() # type: ignore
oauth = OAuth()
oauth.register(
    "auth0",
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    server_metadata_url=f"https://{settings.DOMAIN}/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid profile email",
    },
)

app = FastAPI()
app.add_middleware(middleware_class=SessionMiddleware, secret_key=settings.SECRET_KEY)
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
            audience=settings.AUDIENCE)
    return RedirectResponse('/')


@app.get("/callback")
async def callback(request: Request):
    token = await oauth.auth0.authorize_access_token(request)
    print(token)
    request.session['access_token'] = token['access_token']
    request.session['id_token'] = token['id_token']
    request.session['userinfo'] = token['userinfo']
    print(request.session['userinfo'])
    return RedirectResponse('/profile')


@app.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(
        url=f"https://"
            f"{settings.DOMAIN}"
            f"/v2/logout?"
            f"{urlencode(
                {
                    'returnTo': request.url_for('/'),
                    'client_id': settings.CLIENT_ID},
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
# Houve um problema com o video, pois mesmo que eu tenha seguido o passo a passo, não consegui fazer o callback funcionar
