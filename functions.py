import wikipedia, random
import os, sys

def config():
    print ("Bienvenido a la configuracion del bot :D\n\n")
    loadconfig = input('Usar configuracion por defecto?(y/n)-->')
    if loadconfig == 'y':
        if os.path.exists('token.txt'):
            fconfig = open('token.txt', 'r')
            lineas = fconfig.readlines()
            token = lineas[0]  
            fconfig.close()
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")
            return token

        else:
            print('Configuracion no detectada')
            print('Creando configuracion')
            loadconfig = 'n'

    if loadconfig == 'n':
        token = input("Ingresa el token-->")     
        fconfig = open('token.txt', 'a')
        fconfig.write(token)
        fconfig.close()
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        return config
        
    else:
        print ('Parametro no valido, intentalo de nuevo.')
        sys.exit()




def definiciones(palabra):
    """Busquedas de definiciones en wikipedia """
    #Config library wikipedia
    wikipedia.set_lang("es")
    
    try: #Obtener la informacion y retornarla
        resumen = wikipedia.summary(palabra, sentences = 1)
        url = (wikipedia.page(palabra).url)
        resultado = (resumen + "\n\nMas info: " + url)
        return resultado
    except: #Si no encuentra la info mensaje de error
        error =  ("No se ha encontrado esta definicion...")
        return error

#Preguntas aleatorias
def add_questions(user_say):
    """Añadir preguntas a la base de datos """
    
    with open("db/questions.txt", "a") as file:
        file.write("\n")
        file.write(user_say)
        file.close()

def read_questions():
    with open("db/questions.txt","r") as file:
        resultado = ("")
        for line in file:
            resultado = resultado + line
        resultado = ("Las preguntas guardadas son:\n\n" + resultado)
        file.close()
        return resultado

def random_questions():
    question = random.choice(open("db/questions.txt").readlines())
    question = ("🛎La pregunta del dia es:🛎\n\n" + question)
    return question

def help():
    pass