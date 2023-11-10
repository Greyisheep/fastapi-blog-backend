from fastapi import FastAPI
from . import models
from .router import blog, user
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router = (blog.router)
app.include_router = (user.router)