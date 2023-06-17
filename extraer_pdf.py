import pytesseract
from pdf2image import convert_from_path
import os
import argparse

def pdf_text(pdf_path):
    # Convertir el archivo PDF a imágenes
    pages = convert_from_path(pdf_path, dpi=300)

    # Crear un directorio temporal para almacenar las imágenes
    image_dir = "images"
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)

    # Guardar cada página del PDF como una imagen en el directorio temporal
    for i, page in enumerate(pages):
        image_path = os.path.join(image_dir, f"page_{i}.jpg")
        page.save(image_path, "JPEG")

    # Convertir cada imagen a texto utilizando Pytesseract
    text = ""
    for i in range(len(pages)):
        image_path = os.path.join(image_dir, f"page_{i}.jpg")
        page_text = pytesseract.image_to_string(image_path)
        text += page_text + "\n"

    # Eliminar las imágenes del directorio temporal
    for image_path in os.listdir(image_dir):
        os.remove(os.path.join(image_dir, image_path))
    os.rmdir(image_dir)

    return text
