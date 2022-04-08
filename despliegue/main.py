import numpy as np
import pandas as pd

# dill: Extiende el módulo pickle de Python para serializar y deserializar objetos
import dill 
from io import BytesIO

# LIBRERIAS PARA API
from fastapi import FastAPI, File
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel # Para trabajar con clase
from transformers import TransformerFechas, TransformerDistancia, TransformerVelocidad

# CREACION Y TITULO DEL API : BLUEBERRY PREDICTOR
app = FastAPI(title="Blueberry Predictor")

# IMPORTAR EL MODELO
with open("lr_model.pkl", "rb") as f:
    model = dill.load(f)