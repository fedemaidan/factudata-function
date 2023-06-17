import pytesseract
from extraer_pdf import pdf_text
from chatgpt_helper import pedirle_datos_a_chatgpt
from PIL import Image
import json
import re
import os
import requests
from io import BytesIO

extra = ".txt_json"
folder_db = "request_db/"

def create_custom_path(path):
    path = path.replace("/","__")
    return folder_db + path + extra

def guardar_json_txt(path, json_txt):
    custom_path = create_custom_path(path)
    with open(custom_path, 'w') as file:
        file.write(json_txt)

def chatgpt_saved(nombre_archivo):
    return None
    custom_path = create_custom_path(nombre_archivo)
    if os.path.exists(custom_path):
        with open(custom_path, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    else:
        return None

def limpiar(texto):
    texto = borrar_previo_json(texto)
    return texto

def borrar_previo_json(texto):

    match = re.search(r'\{', texto)
    
    if match:
        # Si encontramos una ocurrencia, retornamos el texto a partir de esa posición
        return texto[match.start():]
    else:
        # Si no encontramos una ocurrencia, retornamos el texto original
        return texto 

def dame_tipo(string):
    return "jpg"
    return string[-3:]

def dame_texto_desde_path(path):
    if (dame_tipo(path) == "pdf" or dame_tipo(path) == "PDF"):
            texto = pdf_text(path)
    else:
        # Abrimos la imagen
        print("Vamos a abrir el path", path)
        response = requests.get(path)
        im = Image.open(BytesIO(response.content))
        texto = pytesseract.image_to_string(im)
    
    return texto

def dame_datos_de_factura(path):
    try:
        texto = dame_texto_desde_path(path)
        # chatgpt_response = chatgpt_saved(path)
        # if not chatgpt_response:
        #     chatgpt_response = pedirle_datos_a_chatgpt(texto)
        #     guardar_json_txt(path, chatgpt_response)
        chatgpt_response = pedirle_datos_a_chatgpt(texto)
        json_txt =  limpiar(chatgpt_response)
        return json.loads(json_txt)
    except Exception as e:
        print(e)
        return { "success": False }