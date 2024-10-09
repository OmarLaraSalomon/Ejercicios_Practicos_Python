
###########################################################
#                                                         #
#   Ejecutar script en la terminal                        #
#   Usar:                                                 #
#     1.  python 01-lista-ordenada.py                     #
#                                                         #
###########################################################



def lista_ordenada(numeros): #la funcion recibe como parametro la lista
    
    return sorted(numeros) #sorted retorna una nueva lista


numeros = [67, 14, 2, 99, 1, 5, 100, 45, 34, 89, 59, 3, 4, 8, 19, 10, 11]
print(lista_ordenada(numeros))  
