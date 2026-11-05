import requests

url = "https://archive-api.open-meteo.com/v1/archive"
parametros = {
    "latitude": 37.7796,
    "longitude": -3.7849,
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Madrid",
}
respuesta = requests.get(url, params=parametros, timeout=30)
respuesta.raise_for_status()
datos = respuesta.json()
temperaturas = datos['daily']["temperature_2m_mean"]
temperaturas_maximas = datos['daily']["temperature_2m_max"]
temperaturas_minimas = datos['daily']["temperature_2m_min"]
diferencia_maximas = [round(abs(temperatura_maxima - temperatura_media), 1) for temperatura_maxima, temperatura_media in zip(temperaturas_maximas, temperaturas)]
diferencia_minimas = [round(abs(temperatura_minima - temperatura_media), 1) for temperatura_minima, temperatura_media in zip(temperaturas_minimas, temperaturas)]
print(diferencia_maximas)
print(diferencia_minimas)