# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:56:01 2024

@author: aritr
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langdetect import detect

app = FastAPI()

class ModelInput(BaseModel):
    lang: str

@app.post('/detection')
async def detection(input_parameters: ModelInput):
    try:
        lang_code = detect(input_parameters.lang)
        return {"detected_language": lang_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))