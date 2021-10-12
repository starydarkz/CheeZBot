import wikipedia, random

def definiciones(palabra):
    """Busquedas de definiciones en wikipedia """
    
    wikipedia.set_lang("es")
    try:
        resumen = wikipedia.summary(palabra, sentences = 1)
        url = (wikipedia.page(palabra).url)
        resultado = (resumen + "\n\nMas info: " + url)
        return resultado
    except:
        #search = wikipedia.search(palabra, results=3)
        error =  ("No se ha encontrado esta definicion...")
        """resultado = ""
        for num in range(len(search)):
            resultado = (resultado + f"{num}-> " + search[num] + "\n")
        resultado = (error + resultado)
        return resultado"""
        return error

#Pregunta del dia
def add_questions(user_say):
    """Añadir preguntas a la base de datos """
    
    with open("db/questions.txt", "a") as file:
        file.write(user_say)
        file.write("\n")
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
