### FastAPI Housing Price ###

API développée avec FastAPI pour prédire le prix d’une maison à partir de ses caractéristiques.
Le modèle de Machine Learning est pré-entraîné et chargé depuis housing_model.pkl.
- Test de déploiement pour un modèle machine learning, non basé sur le réel - 

=> Fonctionnalités

Endpoint /predict qui prend en entrée un JSON avec les caractéristiques du logement.

Validation des entrées grâce à Pydantic.

Retourne le prix prédit au format JSON.

Compatible avec CORS → permet au frontend (par ex. FrontEnd_housingprice
) d’appeler l’API.

=> Structure du projet
FastApi_HousingPrice/
│── Dockerfile           # Fichier de configuration pour containerisation
│── housing_model.pkl    # Modèle de ML sauvegardé
│── mainhousing.py       # Code principal FastAPI
│── requirements.txt     # Dépendances Python
│── README.md            # Documentation du projet

⚙ Installation locale

Clone le projet :

git clone https://github.com/LineOr/FastApi_HousingPrice.git
cd FastApi_HousingPrice


Crée et active un environnement virtuel (optionnel mais conseillé).

Installe les dépendances :

pip install -r requirements.txt


Lance l’API :

uvicorn mainhousing:app --reload


Ouvre dans ton navigateur :

http://127.0.0.1:8000/docs

=> Exemple d’appel API
Requête POST

URL : /predict
Body (JSON) :

{
  "MedInc": 4.5,
  "HouseAge": 20,
  "AveRooms": 6.2,
  "AveBedrms": 1.0,
  "Population": 300,
  "AveOccup": 3.2,
  "Latitude": 34.21,
  "Longitude": -118.45
}

Réponse
{
  "prediction": 256789.45
}

=> Utilisation avec Docker

Construire l’image :

docker build -t fastapi-housingprice .


Lancer le conteneur :

docker run -p 8000:8000 fastapi-housingprice


API dispo sur http://localhost:8000 

=> Liens utiles

Frontend associé : FrontEnd_housingprice
