from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.stock_data import get_stock_data
from app.stock_model import predict_stock_price

app = FastAPI()

class StockRequest(BaseModel):
    stock_symbol: str
    start_date: str
    end_date: str

@app.post("/get_stock_data/")
def get_stock_data_endpoint(request: StockRequest):
    stock_data = get_stock_data(request.stock_symbol, request.start_date, request.end_date)
    return stock_data.to_dict()

@app.post("/predict_stock_price/")
def predict_stock_price_endpoint(request: StockRequest):
    predicted_stock_price = predict_stock_price(request.stock_symbol, request.start_date, request.end_date)
    return {"predicted_price": predicted_stock_price.tolist()}
