def separar_letras(palabra): #Función encargada de separar las letras de una palabra o frase
    letras = list(palabra) #Almacena las letras separadas en una lista. Ej: ['h','o','l','a']
    return letras #Retorna la variable letras

def unir_letras(palabra): #Función encargada de la conversion de una lista a una palabra o frase
    palabra_completa = ''.join(palabra)  #Variable que almacena la conversion de la lista a una palabra o frase. ['h','o','l','a'] <-----> hola

    print("\nTexto escrito al revés:",palabra_completa) #Imprime la lista transformada en palabra o frase

print("\n\n\t-------------------HERRAMIENTA PARA ESCRIBIR AL REVÉS-------------------\n")
palabra = input("Ingrese una palabra o texto: ") #Pide al usuario ingresar información
letras_separadas = separar_letras(palabra) #Se llama a la función 'separar_letras' y se le da de parametro el dato ingresado por el usuario
print("\nTexto original:", palabra) #Muestra el texto ingresado por el usuario
letras_separadas.reverse() #El método 'reverse()' invierte la lista.  ['h','o','l','a'] <----->  ['a','l','o','h']
unir_letras(letras_separadas) #Se llama la función 'unir_letras' y se le da de parametro la lista invertida. ['a','l','o','h'] <-----> aloh
input("\n\nPresione ENTER para finalizar el programa....")

#by Arthurlink
