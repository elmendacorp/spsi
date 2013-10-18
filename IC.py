#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jose Miguel Colella


import string

# Constante que contiene las minusculas
# Hay 27 caracteres en el alfabeto
ALPHABET_LOWERCASE = string.ascii_lowercase + "ñ"


def cleanText(text):
    """
    Función creada para reemplazar los caracteres peculiares
    del lenguaje castellano
    """
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")
    text = text.replace("ü", "u")
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace(";", " ")
    text = text.replace(":", " ")
    text = text.replace("!", " ")
    text = text.replace("¡", " ")
    text = text.replace("?", " ")
    text = text.replace("¿", " ")
    # Todo el texto a minuscula
    text = text.lower()
    return text


def eraseWhiteSpace(text):
    """
    Función que elimina los espacios en blanco
    """
    # Con esto quitamos los espacios
    text = ''.join(text.split())
    return text


def countLetterFrecuency(text):
    # Para contar la frecuencia de las letras usamos lo siguiente
    for i in ALPHABET_LOWERCASE:
        print("Frecuencia de las letras")
        print(i + ": " + str(textStr.count(i)))

if __name__ == '__main__':
    fichero = open("test.txt")
    textStr = fichero.read()

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = cleanText(textStr)
    print(textStr)

    # Segundo quitamos los espacios
    textStr = eraseWhiteSpace(textStr)
    print(textStr)

    countLetterFrecuency(textStr)
