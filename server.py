from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import client
from routers.core import router as core_router
app=FastAPI(title="Afuopulse")
api=APIRouter(prefix="/api"); api.include_router(core_router)
@api.get("/")
async def root(): return {"service":"Afuopulse","ok":True}
app.include_router(api)
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=False,allow_methods=["*"],allow_headers=["*"])
@app.on_event("shutdown")
async def shutdown(): client.close()
