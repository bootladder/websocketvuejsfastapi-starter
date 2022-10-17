from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        i = 0
        while True:
            i = i+1
            await asyncio.sleep(1)
            await websocket.send_text('{"another_'+str(i)+':"yayval"}')
    except Exception as e:
        print(e)
    finally:
        await websocket.close()

