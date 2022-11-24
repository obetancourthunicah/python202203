from api.weatherapi import get_weather_api_data
from dao.weather_dao import weather_dao
from utils.cli_parser import run_args
# from <carpeta>.<archivo> import <funcion|clase|variable|constante>

# Parsear argumentos de la linea de comandos
print("Cargando Configuraciones")
args = run_args()
print(args.action)
print("Obteniendo datos de ciudades")
ciudades = ["Tegucigalpa","London","Tokyo"]
fecha = "2022-11-21"
weather_obj = weather_dao()
# weather_dao weather_obj = new weather_dao()
print("="*60)
if args.action == "write":
  datos = list()
  for ciudad in ciudades:
    print("Datos de " + ciudad)
    datos.append(get_weather_api_data(ciudad, fecha))
  print(datos)
  print("Iniciando Guardado en DB")
  for data in datos:
    weather_obj.addOne(data["name"], data["country"], data["tz_id"], data["region"], data["lat"], data["lon"])
elif args.action == "read":
  print("Cargando Data de DB")
  print(weather_obj.getAll())


print("Done!!!!!")
