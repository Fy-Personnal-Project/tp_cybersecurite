from fastapi import FastAPI
from apps.security_application.controllers import user_controller
from config.database import sync_engine
from apps.security_application.domains.entities.Base import Base

app = FastAPI()

Base.metadata.create_all(bind=sync_engine)

app.include_router(user_controller.router)

