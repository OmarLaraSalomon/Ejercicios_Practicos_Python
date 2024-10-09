
###########################################################
#   *Leer.txt es el archivo que se va analizar            #
#                                                         #
#   Ejecutar script en la terminal                        #
#   Usar:                                                 #
#     1.  python 02-leer-archivo.py                       #
#                                                         #
###########################################################

def contar_palabras(archivo):
    
    try:
    #with= cierra el archivo despues de usarlo
        with open(archivo, 'r', encoding='utf-8') as file:#abrir el archivo en lectura con alias
        
            contenido = file.read() #leer el archivo
            palabras = contenido.split()#dividir las palabras
        
        return len(palabras) #longitud 
    
    except FileNotFoundError: #si falla informar
        return "El archivo no fue encontrado."


archivo = "./leer.txt" #ruta del archivo

print(f"El archivo contiene {contar_palabras(archivo)} palabras.")
