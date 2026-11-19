import requests
import math

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
temperaturas_medias = datos['daily']["temperature_2m_mean"]
temperaturas_maximas = datos['daily']["temperature_2m_max"]
temperaturas_minimas = datos['daily']["temperature_2m_min"]
fechas = datos['daily']['time']

media_temperaturas_medias = round(sum(temperaturas_medias) / len(temperaturas_medias), 1)
media_temperaturas_maximas = round(sum(temperaturas_maximas) / len(temperaturas_maximas), 1)
media_temperaturas_minimas = round(sum(temperaturas_minimas) / len(temperaturas_minimas), 1)

mediana_temperaturas_medias = sorted(temperaturas_medias)[len(temperaturas_medias) // 2]
mediana_temperaturas_maximas = sorted(temperaturas_maximas)[len(temperaturas_maximas) // 2]
mediana_temperaturas_minimas = sorted(temperaturas_minimas)[len(temperaturas_minimas) // 2]

mayor_temperatura_media, menor_temperatura_media = max(temperaturas_medias), min(temperaturas_medias)
mayor_temperatura_maxima, menor_temperatura_maxima = max(temperaturas_maximas), min(temperaturas_maximas)
mayor_temperatura_minima, menor_temperatura_minima = max(temperaturas_minimas), min(temperaturas_minimas)

rango_temperatura_media = mayor_temperatura_media - menor_temperatura_media
rango_temperatura_maxima = mayor_temperatura_maxima - menor_temperatura_maxima
rango_temperatura_minima = mayor_temperatura_minima - menor_temperatura_minima

varianza_temperaturas_medias = round(sum((temperatura - media_temperaturas_medias) ** 2 for temperatura in temperaturas_medias) / len(temperaturas_medias), 1)
varianza_temperaturas_maximas = round(sum((temperatura - media_temperaturas_maximas) ** 2 for temperatura in temperaturas_maximas) / len(temperaturas_maximas), 1)
varianza_temperaturas_minimas = round(sum((temperatura - media_temperaturas_minimas) ** 2 for temperatura in temperaturas_minimas) / len(temperaturas_minimas), 1)

desviacion_tipica_temperaturas_medias = round(math.sqrt(varianza_temperaturas_medias), 1)
desviacion_tipica_temperaturas_maximas = round(math.sqrt(varianza_temperaturas_maximas), 1)
desviacion_tipica_temperaturas_minimas = round(math.sqrt(varianza_temperaturas_minimas), 1)

temperaturas_medias_con_fecha = dict(zip(fechas, temperaturas_medias))
primera_semana = list(temperaturas_medias_con_fecha.items())[:7]
segunda_quincena = list(temperaturas_medias_con_fecha.items())[15:]