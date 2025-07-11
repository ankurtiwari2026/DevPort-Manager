from authlib.integrations.starlette_client import OAuth
from fastapi import Request
import os
from dotenv import load_dotenv

load_dotenv()

oauth = OAuth()
oauth.register(
    name='github',
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'read:user repo'}
)

async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.github.authorize_redirect(request, redirect_uri)

async def auth(request: Request):
    token = await oauth.github.authorize_access_token(request)
    user = await oauth.github.get('user', token=token)
    return user.json(), token['access_token']
