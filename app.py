from fastapi import FastAPI, Form, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
from tensorflow.keras.models import load_model 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from gemini01 import main
from weather import generate_weather_html
import requests
import re


app = FastAPI()
templates = Jinja2Templates(directory="templates")
model = load_model("Crop_Recommendation-new.h5")

# Load any scalers if needed
# sc = StandardScaler()
# sc.fit(X_train)
# ms = MinMaxScaler()
# ms.fit(X_train)


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("HomePage.html", {"request": request})

@app.get('/inputform')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/weather_forcasts")
# async def get_weather_html(request: Request, city: str = Form(...)):
#     html_content = generate_weather_html(city)
#     return templates.TemplateResponse("WeatherForcasts.html", {"request": request, "html_content" : html_content})
    

@app.get("/weather_forcasts", response_class=HTMLResponse)
async def get_weather_html(city: str = Query(...)):
    weather_forcast = generate_weather_html(city)
    return weather_forcast

@app.get("/geminiResponse", response_class=HTMLResponse)
async def geminiResponse(Crop : str = Query(...)):
        geminiResult = main(Crop)
        return geminiResult

@app.post("/predict")
async def predict(request: Request, Nitrogen: float = Form(...), Phosporus: float = Form(...),
                  Potassium: float = Form(...), Temperature: float = Form(...), Humidity: float = Form(...),
                  Ph: float = Form(...), Rainfall: float = Form(...)):
    feature_list = [Nitrogen, Phosporus, Potassium, Temperature, Humidity, Ph, Rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    prediction = model.predict(single_pred)

    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}


    if int(np.argmax(prediction)) + 1 in crop_dict:
        crop = crop_dict[int(np.argmax(prediction)) + 1]
        result = f"{crop} is the best crop to be cultivated right there"
        geminiResult = main(crop)


    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    return templates.TemplateResponse("predict.html", {"request": request, "result": result,})# "html_content": geminiResult})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    
