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
        
        res = query(database[key], cmd)
        return res
    except Exception as e:
        print(f"[!] Error message: {e}")
        return {"status": "fail"}

def todo():
    os.system("clear")
    print("[*] Web crawler start")
    
    data = {}
    
    while True:
        flag = False
        try:
            toCrawl = None
            print("[>] Data source (c/currently, p/specify_path, d/defualt, other/exit): ", end="")
            toCrawl = input()
            
            if toCrawl.lower() == "c" or toCrawl.lower() == "currently":
                try_cnt = 0
                while True:
                    try:
                        try_cnt += 1
                        if try_cnt > 5:
                            print("[!] Some unusual errors occurred")
                            print("[!] Exit")
                            exit()
                        data = crawler(email, password)
                        print("[v] Web crawler success :)")
                        flag = True
                        break
                    except Exception as e:
                        print()
                        os.system("clear")
                        print("[!] Web crawler fail :(")
                        print(f"[!] Error message: {e}")
                        print("[!] Retry after 5 seconds")
                        time.sleep(5)
                        print()
                        os.system("clear")
            elif toCrawl.lower() == "p" or toCrawl.lower() == "specify_path":
                print("[>] Specify path: ", end="")
                excel_file_path = input()
                
                excel_data = pd.read_excel(excel_file_path)
                data = excel_data.to_dict(orient='records')
                break
            elif toCrawl.lower() == "d" or toCrawl.lower() == "default":
                print(f"[*] Open {defalut_path}")
                
                excel_data = pd.read_excel(defalut_path)
                data = excel_data.to_dict(orient='records')
                break
            else:
                print("[!] Exit")
                exit()
            
            if flag: break
        except Exception as e:
            print(f"[!] {e}")
    
    query(data)
    
    print("[!] Exit")
    exit()
