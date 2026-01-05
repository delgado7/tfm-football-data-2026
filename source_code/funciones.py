import requests
from google.colab import userdata
import json

def req_football_api(endpoint:str, params:dict={}, host_url:str=X_RAPIDAPI_HOST, key:str=KEY):

  """
  Realiza una llamada a la API de Football-API y devuelve la respuesta en formato JSON.

  Esta función construye una URL para la API de Football-API utilizando el endpoint
  proporcionado y el host por defecto. Configura los encabezados HTTP necesarios
  incluyendo la clave de la API para la autenticación. Maneja varios tipos de errores
  HTTP y de conexión, imprimiendo mensajes informativos en caso de fallo.
  En caso de éxito, imprime un mensaje de éxito y un formato JSON de la respuesta.

  Parámetros:
  ----------
  endpoint : str
      El endpoint específico de la API al que se desea llamar (ej. 'leagues', 'teams').
  params : dict, opcional
      Un diccionario de parámetros de consulta a incluir en la URL de la solicitud (por defecto es {}).
  host_url : str, opcional
      La URL del host de la API (por defecto es X_RAPIDAPI_HOST).
  key : str, opcional
      La clave de la API para la autenticación (por defecto es KEY).

  Retorna:
  ------
  dict
      Un diccionario que contiene la respuesta JSON de la API en caso de éxito,
      o None si ocurre un error.
  """

  url = f"https://{host_url}/{endpoint}"

  headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'x-rapidapi-host': X_RAPIDAPI_HOST,
    'x-rapidapi-key': KEY
  }

  try:
      response = requests.get(url, headers=headers)
      response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
      data = response.json()
      print("API Call Successful!")
  except requests.exceptions.HTTPError as http_err:
      print(f"HTTP error occurred: {http_err}")
  except requests.exceptions.ConnectionError as conn_err:
      print(f"Connection error occurred: {conn_err}")
  except requests.exceptions.Timeout as timeout_err:
      print(f"Timeout error occurred: {timeout_err}")
  except requests.exceptions.RequestException as req_err:
      print(f"An error occurred: {req_err}")
  finally:
      print("API Call completed.")

  return data['response']

def print_json(json_data):
  """
  Imprime datos JSON en un formato legible y con sangría.
  Si los datos contienen una clave 'response' que es una lista, solo se muestran los primeros 5 elementos.

  Parámetros:
  ----------
  json_data : dict o list
      Los datos JSON a imprimir.
  """
  if json_data and 'response' in json_data and isinstance(json_data['response'], list):
      print(json.dumps(json_data['response'][:5], indent=2))
  elif isinstance(json_data, list):
      print(json.dumps(json_data[:5], indent=2))
  else:
      print(json.dumps(json_data, indent=2))

def save_json(data, filename: str, path: str):
  """
  Guarda datos en formato JSON en un archivo específico dentro de una ruta determinada.

  Parámetros:
  ----------
  data : dict o list
      Los datos a guardar en formato JSON.
  filename : str
      El nombre del archivo JSON (ej. 'leagues.json').
  path : str
      La ruta del directorio donde se guardará el archivo (ej. '/content/drive/MyDrive/TFM/Prototipo').
  """
  file_path = f'{path}/{filename}'
  try:
    with open(file_path, 'w') as f:
      json.dump(data, f, indent=2)
    print(f"Data successfully saved to {file_path}")
  except IOError as e:
    print(f"Error saving file to {file_path}: {e}")