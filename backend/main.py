from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from github_auth import login, auth
from sync import sync_repos
from generate_pdf import generate_pdf
from models import Project
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Welcome to DevPort Manager"}

@app.get("/login")
async def github_login(request: Request):
    return await login(request)

@app.get("/auth")
async def github_auth(request: Request):
    user, token = await auth(request)
    sync_repos(token)
    return RedirectResponse("/projects")

@app.get("/projects")
def list_projects():
    db = SessionLocal()
    projects = db.query(Project).all()
    db.close()
    return projects

@app.get("/pdf")
def download_pdf():
    generate_pdf()
    return {"msg": "PDF generated as portfolio_report.pdf"}

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

# Add this line with your own secret key
app.add_middleware(SessionMiddleware, secret_key="your_secret_session_key")

