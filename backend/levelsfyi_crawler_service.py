import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import bs4
import requests
import time
from datetime import datetime
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

from levelsfyi_crawler_module import *

import json
import pickle

from fastapi import FastAPI, HTTPException, Request
from starlette.status import HTTP_202_ACCEPTED

load_dotenv()


email = os.getenv("EMAIL")
password = os.getenv("PASSWD")


defalut_path = "../FAANGN_24-12-2023-06-41-20.xlsx"

app = FastAPI()
database = {}

@app.get("/health")
def health_check():
    # check the health of the server
    return {"status": "ok"}

@app.post("/crawler")
async def callcrawler(request: Request):
    try:
        print("[v] call crawler")
        req_data = await request.json()
        print(req_data)
        
        action = req_data["action"]
        key = req_data["key"]
        
        if action.lower() == "crawler":
            print("[v] go to crawler")
            # data = crawler(email, password)
            # print(type(data))
            return {"status": "go to crawler"}
        elif action.lower() == "default":
            print("[v] go to default")
            excel_data = pd.read_excel(defalut_path)
            data = excel_data.to_dict(orient='records')
            data_with_nan_as_str = [{k: "nan" if isinstance(v, float) and pd.isna(v) else v for k, v in entry.items()} for entry in data]
            database[key] = data_with_nan_as_str
            print(type(database[key]))
            print(database[key])
            return {"status": "go to default"}
        else:
            return {"status": "action is invalid"}
    except Exception as e:
        print(f"[!] Error message: {e}")
        return {"status": "fail"}

@app.post("/query")
async def callquery(request: Request):
    try:
        print("[v] call query")
        req_data = await request.json()
        print(f"[v] req_data: {req_data}")
        
        cmd = req_data["cmd"]
        key = req_data["key"]
        
        res = query(database[key], cmd, key)
        return res
    except Exception as e:
        print(f"[!] Error message: {e}")
        return {"status": "fail"}