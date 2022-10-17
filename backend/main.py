import html
import json
from fastapi import FastAPI, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import traceback


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5090",
    "http://localhost:5080",
    "http://localhost:6080",
    "http://localhost:6090",
]

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


#######
# JSON API
#

# GET THE MODEL

@app.post("/2022/balancereportjson")
async def balancereportjson_2022(info : Request):

	#requestjson = await info.json()
	#balancereportjsonstring = ledgercontroller.getBalanceReportJsonString(requestjson)

	#myjson = json.loads(balancereportjsonstring )
	myjson = json.loads("hello" )
	return JSONResponse(content=myjson, status_code=201)

# WRITE THE MODEL
