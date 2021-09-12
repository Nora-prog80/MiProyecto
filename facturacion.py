# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:10:17 2021

@author: Nora
"""
cod_P1 = 1010
P1 = "Camisas"
cantidad = 10
precio_P1_conIVA = 116000
IVA_P1 = precio_P1_conIVA*0.16

TT_P1 = cantidad * precio_P1_conIVA
Sub_P1 = TT_P1 -(IVA_P1/100)

cod_P2 = 1010
P2 = "Pantalones"
precio_P2_conIVA = 119000
cantidad = 10
IVA_P2 = precio_P2_conIVA* 0.19

TT_P2 = cantidad * precio_P2_conIVA
Sub_P2 = TT_P2 -(IVA_P2/100)

print("****************************************************************************")
print("                     EMPRESA COLOMBIANA DE TEXTILES S.A                     ")
print( )
print("Código","\t Producto", "\t \t Cantidad", "\tPrecio Unitario", "\t IVA producto", "\tTotal")
print(cod_P1, "\t", P1, "\t \t", cantidad, "\t \t", precio_P1_conIVA, "\t \t \t", IVA_P1, "\t \t", TT_P1)
print(cod_P2, "\t", P2, "\t", cantidad, "\t \t", precio_P2_conIVA, "\t \t \t", IVA_P2, "\t \t", TT_P2)
print( )
print("Total compra: \t", "$", TT_P1+TT_P2 )
print( )
print("****************************************************************************")