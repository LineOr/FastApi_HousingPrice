from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


#Chargement du modèle au démarrage de l'application
model = joblib.load("housing_model.pkl")



#Créez un endpoint /predict qui prend en entrée un objet JSON contenant 
#les différentes caractéristiques de la maison (par exemple, {'surface': 150, 
#'bedrooms': 3, 'bathrooms': 2}). Utilisez un Pydantic BaseModel pour 
#valider les données d'entrée.
# ◦ Dans la fonction de cet endpoint, utilisez le modèle pour faire une prédiction 
#de prix.
# ◦ Renvoie le prix prédit au format JSON

class Housing(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


#Initialisation de l'application FastAPI


app = FastAPI()

origins = [
    "http://localhost:5500",
    "https://frontend-housingprice.onrender.com",
    # Ajoutez d'autres origines autorisées si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict_housing(housing_data: Housing):
    #Conversion des données d'entrée en format tableau numpy
    data = np.array([
        housing_data.MedInc,
        housing_data.HouseAge,
        housing_data.AveRooms,
        housing_data.AveBedrms,
        housing_data.Population,
        housing_data.AveOccup,
        housing_data.Latitude,
        housing_data.Longitude
    ]).reshape(1, -1)

    
    
    #Prédiction
    prediction = model.predict(data)
    return {"predicted_price": float(prediction)}
