from fastapi import FastAPI
from .auth import routes as auth_routes, models as auth_models
from .posts import routes as post_routes, models as post_models
from .db.database import engine

auth_models.Base.metadata.create_all(engine)
post_models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(auth_routes.api_router)
app.include_router(post_routes.api_router)



