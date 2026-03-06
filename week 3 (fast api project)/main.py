from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI(title="Ammar FastAPI Project")

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/fastapi"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

import user_router

base.metadata.create_all(bind=engine)
app.include_router(user_router.router)