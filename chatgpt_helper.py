import requests
import json
import os

token = os.getenv('chatgpt_token')

def dame_prompt(texto):
    prompt = "Considerando la siguiente factura: ' \n"
    prompt += texto
    prompt += "Extrae los valores en formato json con las siguientes keys \"nombre_emisor\",\"condicion_iva\" , \"numero_factura\" , \"fecha\", \"valor_neto_sin_iva\" y \"total\" . Utiliza \" para los valores y claves"
    return prompt

def pedirle_datos_a_chatgpt(texto):
    prompt = dame_prompt(texto)
    url = "https://api.openai.com/v1/completions"

    # Definir los parámetros de la solicitud
    params = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.2
    }
    
    # Agregar la clave de API a los encabezados de la solicitud
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
    
    # Realizar la solicitud a la API de ChatGPT
    response = requests.post(url, headers=headers, data=json.dumps(params))
    
    # Obtener la respuesta de la API
    if response.status_code == 200:
        data = json.loads(response.text)
        respuesta = data["choices"][0]["text"]
        return respuesta
    else:
        print("Ocurrió un error al hacer la solicitud a la API")
        print(response)
        return None
