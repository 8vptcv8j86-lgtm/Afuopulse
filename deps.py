import re
from datetime import datetime, timezone, timedelta
from typing import Optional
import bcrypt, jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from db import db, JWT_SECRET

bearer = HTTPBearer(auto_error=False)
def now_dt(): return datetime.now(timezone.utc)
def now_iso(): return now_dt().isoformat()
def hash_pw(v): return bcrypt.hashpw(v.encode(), bcrypt.gensalt()).decode()
def verify_pw(v,h):
    try: return bcrypt.checkpw(v.encode(), h.encode())
    except Exception: return False
def make_token(uid):
    return jwt.encode({"sub":uid,"iat":now_dt(),"exp":now_dt()+timedelta(days=30)},JWT_SECRET,algorithm="HS256")
async def get_current_user(creds: Optional[HTTPAuthorizationCredentials]=Depends(bearer)):
    if not creds: raise HTTPException(401,"Missing token")
    try: uid=jwt.decode(creds.credentials,JWT_SECRET,algorithms=["HS256"]).get("sub")
    except Exception: raise HTTPException(401,"Invalid token")
    user=await db.users.find_one({"id":uid},{"_id":0,"password":0})
    if not user: raise HTTPException(401,"User not found")
    return user
async def require_officer(user=Depends(get_current_user)):
    if user.get("role")!="officer": raise HTTPException(403,"Officer role required")
    return user
async def require_gov(user=Depends(get_current_user)):
    if user.get("role") not in {"government","officer"}: raise HTTPException(403,"Government or officer role required")
    return user
def sanitize_prompt(v):
    for p in [r"ignore (all|previous) instructions",r"system prompt",r"jailbreak",r"reveal (the )?prompt"]:
        v=re.sub(p,"[filtered]",v,flags=re.I)
    return v.strip()[:2000]
