from github import Github
from models import Project
from database import SessionLocal
from sqlalchemy.orm import Session

def sync_repos(access_token: str):
    db: Session = SessionLocal()
    g = Github(access_token)
    user = g.get_user()
    repos = user.get_repos()

    for repo in repos:
        existing = db.query(Project).filter(Project.name == repo.name).first()
        if not existing:
            project = Project(
                name=repo.name,
                description=repo.description,
                github_url=repo.html_url,
                stars=repo.stargazers_count,
                language=repo.language,
                featured=False
            )
            db.add(project)
    db.commit()
    db.close()
