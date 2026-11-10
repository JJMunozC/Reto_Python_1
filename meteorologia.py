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
fechas = datos['daily']['time']
diccionario = {fecha : {"media" : temperatura_media, "máxima" : temperatura_maxima, "mínima" : temperatura_minima} 
               for fecha, temperatura_media, temperatura_maxima, temperatura_minima in 
               zip(fechas, temperaturas, temperaturas_maximas, temperaturas_minimas)}
media_mas_alta = max(diccionario, key=lambda fecha: diccionario[fecha]["media"])
print(media_mas_alta)

#amplitud_termica = {fecha : (temperatura_maxima - temperatura_minima) for fecha, _, temperatura_maxima, temperatura_minima in diccionario.items()}
print(diccionario.items())