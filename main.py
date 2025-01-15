from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import webhook, onboarding, users



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])



app.include_router(webhook.router)
app.include_router(onboarding.router)
app.include_router(users.router)

@app.get('/')
async def get_root():
    return {"welcome to crowwd bank"}

@app.get("/healthcheck")
async def check():
    return True


