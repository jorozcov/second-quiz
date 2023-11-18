from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery
import os

app = FastAPI()

origins = ["http://localhost:9000", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["GET", "OPTIONS"],
)



def get_db_client():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "second_submission_julian_service.json"
    return bigquery.Client()

def prepare_query(WeeksFrom, WeeksTo, AgeFrom, AgeTo, WeightFrom, WeigthTo):
    return f"""SELECT EXTRACT(YEAR FROM Year) AS Year, SUM(Births) AS Total
        FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality` 
        WHERE (Ave_OE_Gestational_Age_Wks BETWEEN {WeeksFrom} AND {WeeksTo}) AND 
        (Ave_Age_of_Mother BETWEEN {AgeFrom} AND {AgeTo}) AND
        (Ave_Birth_Weight_gms BETWEEN {WeightFrom} AND {WeigthTo})
        group by Year"""

@app.get("/")
async def root():
    return {"message": "Hola"}

@app.get("/{WeeksFrom}_{WeeksTo}_{AgeFrom}_{AgeTo}_{WeightFrom}_{WeigthTo}")
async def get_query(WeeksFrom:int, WeeksTo:int, AgeFrom:int, AgeTo:int, WeightFrom:int, WeigthTo:int):
    query = prepare_query(WeeksFrom, WeeksTo, AgeFrom, AgeTo, WeightFrom, WeigthTo)
    client = get_db_client()
    query_job = client.query(query)
    result = query_job.to_dataframe()
    
    return result.to_json(orient="records")