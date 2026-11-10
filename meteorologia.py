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
dias_frios = [temperatura for temperatura in temperaturas if temperatura < 10]
dias_templados = [temperatura for temperatura in temperaturas if temperatura >= 10 and temperatura <= 20]
dias_calidos = [temperatura for temperatura in temperaturas if temperatura > 20]
print(dias_frios)
print(dias_templados)
print(dias_calidos)