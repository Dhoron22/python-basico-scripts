# script_basico.py - Análisis simple de datos

# Lectura de datos
nombres = ["Juan", "María", "Pedro", "Ana"]
edades = [25, 30, 22, 28]

# Procesamiento
promedio_edad = sum(edades) / len(edades)
persona_mayor = nombres[edades.index(max(edades))]

# Salida
print(f"El promedio de edad es: {promedio_edad}")
print(f"La persona de mayor edad: {persona_mayor}")

# Bonus: uso de librería
import datetime
print(f"Análisis realizado el: {datetime.datetime.now()}")
