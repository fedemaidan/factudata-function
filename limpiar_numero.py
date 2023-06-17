import locale

# Resto de tu código aquí

def indicador_centavos(cadena):
    indicador = cadena[-3]

    if indicador == ',' or indicador == ',':
        return indicador
    else:
        indicador = cadena[-2]
        if indicador == ',' or indicador == ',':
            return indicador
    
    return ""


def str_to_float(string):
    try:
        float_number = float(string)
        return float_number
    except ValueError:
        print("El valor ingresado no es un número")

def limpiar_numero(numero_string):
    indicador = indicador_centavos(numero_string)
    numero_string = numero_string.replace("$","")

    if indicador == ',':
        locale.setlocale(locale.LC_ALL, 'es_ES.utf8') 
        numero_string = numero_string.replace(".","")
        numero_float = locale.atof(numero_string)    
    else:
        numero_string = numero_string.replace(",","")
        numero_float = str_to_float(numero_string)

    return numero_float


