import numpy as np
import pandas as pd

# dill: Extiende el módulo pickle de Python para serializar y deserializar objetos
import dill 
from io import BytesIO

# LIBRERIAS PARA API
from fastapi import FastAPI, File
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel # Para trabajar con clase

# CREACION Y TITULO DEL API : BLUEBERRY PREDICTOR
app = FastAPI(title="Blueberry Predictor")

# DESHABILITAR EL CORS PARA CONSULTAS LOCALHOST
origins = [ "*",]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

# IMPORTAR EL MODELO
with open("model.pkl", "rb") as f:
    model = dill.load(f)

# PRIMER ENDPOINT: GET ENDPOINT
@app.get("/", response_class=JSONResponse)
def get_funct(
    fruitset: float,
    RainingDays: float,
    AverageTempBS: float,
    osmiaBee: float,
    bumblesBee: float,
    andrenaBee: float,
    honeyBee: float,
    clonesize: float,
):
    df = pd.DataFrame(
        [
            [
                fruitset,
                RainingDays,
                AverageTempBS,
                osmiaBee,
                bumblesBee,
                andrenaBee,
                honeyBee,
                clonesize,
            ]
        ],
        columns=[
            "fruitset",
            "RainingDays",
            "AverageTempBS",
            "osmiaBee",
            "bumblesBee",
            "andrenaBee",
            "honeyBee",
            "clonesize",
        ],
    )
    prediction = model.predict(df)
    return {
        "features": {
            "fruitset": fruitset,
            "RainingDays": RainingDays,
            "AverageTempBS": AverageTempBS,
            "osmiaBee": osmiaBee,
            "bumblesBee": bumblesBee,
            "andrenaBee": andrenaBee,
            "honeyBee": honeyBee,
            "clonesize": clonesize,
        },
        "prediction": list(prediction)[0],
    }

if __name__ == "__main__":
    import uvicorn

    # For local development:
    # Para correr la aplicación en desarrollo local:
    uvicorn.run("main:app", port=3000, reload=True)
    

# SEGUNDO ENDPOINT: POST ENDPOINT
class Blueberry(BaseModel):
    fruitset: float
    RainingDays: float
    AverageTempBS: float
    osmiaBee: float
    bumblesBee: float
    andrenaBee: float
    honeyBee: float
    clonesize: float

@app.post("/json", response_class=JSONResponse)
def post_json(blueberry: Blueberry):
    fruitset = blueberry.fruitset
    RainingDays = blueberry.RainingDays
    AverageTempBS = blueberry.AverageTempBS
    osmiaBee = blueberry.osmiaBee
    bumblesBee = blueberry.bumblesBee
    andrenaBee = blueberry.andrenaBee
    honeyBee = blueberry.honeyBee
    clonesize = blueberry.clonesize

    df = pd.DataFrame(
        [
            [
                fruitset,
                RainingDays,
                AverageTempBS,
                osmiaBee,
                bumblesBee,
                andrenaBee,
                honeyBee,
                clonesize,
            ]
        ],
        columns=[
            "fruitset",
            "RainingDays",
            "AverageTempBS",
            "osmiaBee",
            "bumblesBee",
            "andrenaBee",
            "honeyBee",
            "clonesize",
        ],
    )
    prediction = model.predict(df)
    return {
        "features": {
            "fruitset": fruitset,
            "RainingDays": RainingDays,
            "AverageTempBS": AverageTempBS,
            "osmiaBee": osmiaBee,
            "bumblesBee": bumblesBee,
            "andrenaBee": andrenaBee,
            "honeyBee": honeyBee,
            "clonesize": clonesize,
        },
        "prediction": list(prediction)[0],
    }
