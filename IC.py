#!/usr/bin/env python3
# coding: utf-8
# Author: Jose Miguel Colella


import string

# Constante que contiene las minusculas
# Hay 27 caracteres en el alfabeto
#ALPHABET_LOWERCASE = string.ascii_lowercase + "ñ"
lista_letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","ñ","n","o","p","q","r","s","t","u","v","w","x","y","z"]
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
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace("!", "")
    text = text.replace("¡", "")
    text = text.replace("?", "")
    text = text.replace("¿", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("/", "")
    text = text.replace("'", "")
    text = text.replace("-", "")
    text = text.replace("\n", "")
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


def countLetterFrecuency(text, textout):
    # Para contar la frecuencia de las letras usamos lo siguiente
    for i in lista_letras:
        a = i + ": " + str(text.count(i))
        textout.write(a)
        textout.write("\n")


if __name__ == '__main__':
    fichero = open("test.txt")
    fichero2 = open("process.txt", "w")
    fichero3 = open("count.txt", "w")
    textStr = fichero.read()

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = eraseWhiteSpace(textStr)
    textStr = cleanText(textStr)
    #NO CAMBIES MAS ESTO
    # Segundo quitamos los espacios

    fichero2.write(textStr)

    countLetterFrecuency(textStr, fichero3)
