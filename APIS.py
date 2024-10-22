import requests
import json

def obtener_clima(ciudad, api_key):
    # URL base de la API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    
    try:
        # Hacer la solicitud a la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verificar si hubo algún error en la solicitud
        datos = respuesta.json()  # Convertir los datos a formato JSON

        # Extraer y mostrar los datos relevantes
        temperatura = datos['main']['temp']
        descripcion_clima = datos['weather'][0]['description']
        humedad = datos['main']['humidity']
        viento = datos['wind']['speed']
        pais = datos['sys']['country']
        
        # Formato de salida mejorado
        print("\n" + "="*40)
        print(f"Clima en {ciudad.capitalize()}, {pais}:")
        print("-"*40)
        print(f"Temperatura: {temperatura}°C")
        print(f"Descripción: {descripcion_clima.capitalize()}")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {viento} m/s")
        print("="*40 + "\n")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Error: {err}")

def main():
    # Aquí deberías ingresar tu API key de OpenWeatherMap
    api_key = "3392e41b87e3ff32b6515b3e8ddd9d1a"

    while True:
        # Obtener la ciudad del usuario
        ciudad = input("Ingresa el nombre de una ciudad (o 'salir' para terminar): ")

        # Verificar si el usuario desea salir
        if ciudad.lower() == "salir":
            print("¡Gracias por usar el programa!")
            break
        
        # Llamar a la función para obtener el clima
        obtener_clima(ciudad, api_key)

# Ejecutar el programa
if __name__ == "__main__":
    main()