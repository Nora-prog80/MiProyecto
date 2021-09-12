# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:02:36 2021

@author: Nora
"""

usuario = input("Escriba el usuario: ")

if usuario == "Nora":
    print("usuario correcto")
    contrasena = input("Escriba la contraseña: ")
    if contrasena == "123abc":
        print("La contraseña es correcta")   
    else:
        print("Contraseña incorrecta")
        print(input("Escriba la contraseña: "))
        if contrasena == "123abc":
            print("contraseña correcta, bienvenido")
            
else:
    print("usuario incorrecto, intento 2 de 3")
    print(input("Escriba el usuario: "))
    print("usuario incorrecto, intento 3 de 3")
    print(input("Escriba el usuario: "))
    print("Intentos superados, lo siento")
   