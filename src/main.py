
from src.config.config import Mode, config
# TODO: ArgParser for Mode
config.load(Mode.DEV)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api.http.routers import router as user_router


app = FastAPI(title="TEAMAPP", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

ROUTERS_V1 = [
    user_router
]

for router in ROUTERS_V1:
    app.include_router(router, prefix="/api/v1")
