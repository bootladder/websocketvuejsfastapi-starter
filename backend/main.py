import html
import json
from fastapi import FastAPI, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import traceback
from fastapi import WebSocket
import asyncio


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#######
# STATIC FILES
#
app.mount("/static", StaticFiles(directory="static"), name="static") 


# GET THE MODEL
@app.post("/getmodel")
async def getmodel(info : Request):
	with open('/data/rolodex.json') as f:
		myjson = json.load(f)
	return JSONResponse(content=myjson, status_code=200)

# WRITE THE MODEL
@app.post("/setmodel")
async def setmodel(info : Request):
	myjson = json.loads("fuck yeah" )
	return JSONResponse(content=myjson, status_code=200)


# WATCH THE FILE
print("yeah serving")

@app.websocket("/ws")
async def websocket_endpoint_log(websocket: WebSocket):
    print("WAT")
    await websocket.accept()
    await websocket.send_text("FUCK YEAH")
    i = 0

    try:
        while True:
            thehash = 0
            with open('/data/rolodex.json') as f:
                myjson = json.load(f)
                newhash = 1

            i = i+1
            await asyncio.sleep(1)
            await websocket.send_text('{"another_'+str(i)+':"dope"}')
    except Exception as e:
        print(e)
    finally:
        print("WTF WHY CLOS")
        await websocket.close()


#@app.websocket("/ws")
#async def websocket_endpoint(websocket: WebSocket):
#    print("started")
#    await websocket.accept()
#    try:
#        while True:
#            data = await websocket.receive_text()
#            print(f"received: {int(data)}")
#            index = int(data)
#            image = get_image(volume, index)
#            await websocket.send_bytes(image)
#    except Exception as e:
#        print(e)
#    finally:
#        websocket.close()
#
