from fastapi import FastAPI
import sqlalchemy as sa
import json
import requests



engine = sa.create_engine("sqlite:///:memory:")
connection = engine.connect()
metadata = sa.MetaData()


api = FastAPI()

@api.get('/')
def index():
    return {'message': "Test return api"}

# python -m uvicorn main:api --reload