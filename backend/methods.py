from fastapi import HTTPException, UploadFile
from fastapi import File as f_file
from fastapi import responses, Request
from fastapi import Response
from pathlib import Path

import os

from main import db, app
from utils import *

from settings import path_To_Files

__all__ = [
    "checkAuth",
    "main_page",
    "http_getFiles",
    "uploadFile",
    "http_getFile",
    "deleteFile"
]

@app.get("/login")
async def checkAuth(request: Request):
    checkSession(request)
    return {"status": "ok"}


@app.post("/register")
async def register(request: Request, response: Response):
    user = getUser(request)

    if (user.id == -1):
        db.insert("users", 
                    ["login", "password", "encryption_key"],
                    [login, hashed_password, genToken()])


@app.post("/login")
async def main_page(request: Request, response: Response):
    data = await request.json()
    login = data.get("login")
    password = data.get("password")

    if (login is None or password is None):
        raise HTTPException(status_code=400, detail="Missed auth data")

    user = getUser(request)
    hashed_password: str = hash_text(password)
    
    print(user.password, hashed_password)
    if (user.password == hashed_password):
        token = genToken()

        # делаем сессию
        db.insert("sessions",
                  ["user_id", "token", "useragent", "ip"],
                  [user.id, token, request.headers.get("user-agent"), request.client.host])

        response.set_cookie(key="token", value=token, max_age=604800, httponly=True)
        response.set_cookie(key="login", value=login, max_age=604800, httponly=True)

        return {"status": "ok"}
    else:
        raise HTTPException(status_code=422, detail="Invalid login or password")


@app.post("/getFiles")
def http_getFiles(request: Request):
    user = getUser(request)
    checkSessionByUser(user.id, request)

    return getFiles(user)


@app.post("/uploadFile")
async def uploadFile(file: UploadFile = f_file(...), request: Request = None):
    server_filename = genToken()
    user = getUser(request)
    checkSessionByUser(user.id, user.login, request)

    Path.touch(path_To_Files + server_filename)
    
    with open(path_To_Files + server_filename, "wb") as fileOut:
        content = await file.read()
        fileOut.write(content)
    
    db.insert("files", 
              ["client_filename", "server_filename", "owner_id"],
              [file.filename, server_filename, user.id])

    return {"client_filename":file.filename, "server_filename":server_filename}


@app.get("/getFile/{server_filename}")
def http_getFile(server_filename: str, request: Request):
    user = getUser(request)

    checkSessionByUser(user, request)

    file = getFile(user, server_filename)

    return responses.FileResponse(filename=file.client_filename, 
                                  path=path_To_Files+server_filename)


@app.delete("/deleteFile/{server_filename}")
def deleteFile(server_filename: str, request: Request):
    user = getUser(request)
    checkSessionByUser(user)

    # проверяем файл, его не будет, то выкенет исключение 404
    getFile(user, server_filename)
    
    os.remove(path_To_Files+server_filename)
    db.execute("delete from files where server_filename = %s", (server_filename,))
