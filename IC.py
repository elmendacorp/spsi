#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jose Miguel Colella


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

    return text


def eraseWhiteSpace(text):
    """
    Función que elimina los espacios en blanco
    """
    # Con esto quitamos los espacios
    text = ''.join(text.split())
    return text


if __name__ == '__main__':
    fichero = open("test.txt")
    textStr = fichero.read()

    # Primero limpiamos el texto de los caracteres peculiares
    textStr = cleanText(textStr)
    print(textStr)

    # Segundo quitamos los espacios
    textStr = eraseWhiteSpace(textStr)
    print(textStr)
