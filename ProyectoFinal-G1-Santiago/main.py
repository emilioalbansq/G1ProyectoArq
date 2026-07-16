import requests
import os
import csv
from datetime import datetime, UTC


SANTIAGO_LAT = -33.45694
SANTIAGO_LONGITUDE = -70.64827
API_KEY = os.getenv("OPENWEATHER_API_KEY")
FILE_NAME = "clima-santiago-hoy.csv"


def get_weather(lat, lon, api):
    '''
    Realiza una consulta al API de OpenWeatherMap utilizando la latitud,
    longitud y API KEY proporcionadas, y devuelve la respuesta en formato JSON.
    '''
    # URL base del API
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Parámetros enviados al API
    parametros = {
        "lat": lat,
        "lon": lon,
        "appid": api,
        "units": "metric",
        "lang": "es"
    }

    # Realiza la petición al servidor
    respuesta = requests.get(url, params=parametros)

    # Convierte la respuesta JSON en un diccionario de Python
    return respuesta.json()


def write2csv(weather, csv_filename):
    '''
    Escribe la información climatológica procesada en un archivo CSV.
    Si el archivo no existe, crea el encabezado automáticamente.
    Cada ejecución agrega un nuevo registro al final del archivo.
    '''

    # Verifica si el archivo ya existe
    existe = os.path.isfile(csv_filename)

    # Abre el archivo en modo agregar
    with open(csv_filename, "a", newline="", encoding="utf-8") as archivo:

        # Crea el escritor utilizando las claves del diccionario
        writer = csv.DictWriter(
            archivo,
            fieldnames=weather.keys()
        )

        # Si el archivo es nuevo escribe el encabezado
        if not existe:
            writer.writeheader()

        # Escribe una nueva fila
        writer.writerow(weather)


def process(json):
    '''
    Procesa la respuesta JSON obtenida desde el API, normaliza la información
    en un diccionario plano y la prepara para ser almacenada en el archivo CSV.
    '''
    # Diccionario donde se almacenarán todos los datos en formato plano
    normalized_dict = {}

    # Fecha y hora de la medición
    normalized_dict["fecha_hora"] = datetime.fromtimestamp(
        json["dt"], UTC
    ).strftime("%Y-%m-%d %H:%M:%S")
    
    # COORDENADAS
    for clave, valor in json["coord"].items():
        normalized_dict["coord_" + clave] = valor

    # INFORMACIÓN PRINCIPAL DEL CLIMA
    for clave, valor in json["main"].items():
        normalized_dict["main_" + clave] = valor

    # VIENTO
    for clave, valor in json["wind"].items():
        normalized_dict["wind_" + clave] = valor

    # NUBES
    for clave, valor in json["clouds"].items():
        normalized_dict["clouds_" + clave] = valor

    # INFORMACIÓN DEL SISTEMA
    for clave, valor in json["sys"].items():
        normalized_dict["sys_" + clave] = valor

    # WEATHER ES UNA LISTA
    if len(json["weather"]) > 0:

        for clave, valor in json["weather"][0].items():
            normalized_dict["weather_" + clave] = valor

    # LLUVIA (puede no existir)
    if "rain" in json:

        for clave, valor in json["rain"].items():
            normalized_dict["rain_" + clave] = valor

    # NIEVE (puede no existir)
    if "snow" in json:

        for clave, valor in json["snow"].items():
            normalized_dict["snow_" + clave] = valor

    # CAMPOS SIMPLES DEL JSON
    normalized_dict["base"] = json["base"]
    normalized_dict["visibility"] = json["visibility"]
    normalized_dict["timezone"] = json["timezone"]
    normalized_dict["id"] = json["id"]
    normalized_dict["name"] = json["name"]
    normalized_dict["cod"] = json["cod"]

    # Retorna el diccionario listo para escribirlo en el CSV
    return normalized_dict


def main():
    print("===== Bienvenido a Santiago-Clima =====")
    santiago_weather = get_weather(lat=SANTIAGO_LAT, lon=SANTIAGO_LONGITUDE, api=API_KEY)
    if santiago_weather['cod']==200:
        weather = process(santiago_weather)
        write2csv(weather, FILE_NAME) 
        print("Datos guardados correctamente.")
    else:
        print("Ciudad no disponible o API KEY no válida")

if __name__ == '__main__':
    main()
