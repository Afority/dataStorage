from hashlib import sha256
from fastapi import Request, HTTPException
from random import choice
import string

from main import db
from classes import User, File

__all__ = [
    "genToken",
    "hash_text",
    "getUser",
    "getFile", 
    "getFiles", 
    "checkSessionByUser", 
    "checkSession"
]

def genToken():
    """
    Генерирует токен для сессии, шифрования файлов и имен файлов
    """
    token = ""
    
    for i in range(32):
        token += choice(string.ascii_letters + string.digits)
    
    return token

def hash_text(plaintext: str):
    return sha256(plaintext.encode()).hexdigest()


def getUser(request: Request) -> User:
    try:
        login = request.cookies.get("login")
        user_id, password, enctypt_key = \
        db.execute("select id, password, encryption_key from users where login = %s;", 
                (login,))[0]
        return User(user_id, login, password, enctypt_key)
    except BaseException as e:
        raise HTTPException(401, "user not found")


def getFile(user: User, server_filename) -> File:
    try:
        client_filename = db.execute(
                      "select client_filename from files "
                      "where owner_id = %s and server_filename = %s", 
                      (user.id, server_filename))[0][0]
        
        return File(client_filename, server_filename)
    except:
        raise HTTPException(404, "file not found")

def getFiles(user: User) -> list[dict]:
    try:
        files_atr = db.execute(
                      "select client_filename, server_filename from files "
                      "where owner_id = %s", (user.id))
        
        files = []
        for file in files_atr:
            files.append({file[0], file[1]})
            
        return files
    except:
        raise HTTPException(404, "files not found")



# нижнее подчеркивание, потому что не используется в основном приложении, 
# а вызываются другие функции checkSessionByUserId и checkSession
def _checkSession(login: str, token: str, user_id: str, user_agent: str, host: str):
    if (login   is None or
        token   is None or
        user_id is None):

        raise HTTPException(401)
    
    if (db.execute("select * from sessions "
                   "where user_id = %s and token = %s and useragent = %s and ip = %s;",
                   (user_id, token, user_agent, host)) is not None):
        HTTPException(401)
    

def checkSessionByUser(user: User, request: Request):
    _checkSession(
        login= user.login, 
        token= request.cookies.get("token"), 
        user_id=user.id, 
        user_agent=request.headers.get("user-agent"),
        host=request.client.host
    )


def checkSession(request: Request):
    user = getUser(request)

    _checkSession(
        login=request.cookies.get("login"), 
        token=request.cookies.get("token"), 
        user_id=user.id, 
        user_agent=request.headers.get("user-agent"),
        host=request.client.host
    )
