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
    definiciones = {
    "threat hunting":"Cyber Threat Hunting\n\nLa caza de amenazas cibernéticas es una actividad de defensa cibernética activa. Es el proceso de búsqueda proactiva e iterativa a través de redes para detectar y aislar amenazas avanzadas que evaden las soluciones de seguridad existentes",
    "cyber threat hunting":"Cyber Threat Hunting\n\nLa caza de amenazas cibernéticas es una actividad de defensa cibernética activa. Es el proceso de búsqueda proactiva e iterativa a través de redes para detectar y aislar amenazas avanzadas que evaden las soluciones de seguridad existentes",
    "hack the box":"Hack The Box \n\nEs una plataforma masiva de capacitación en ciberseguridad en línea, que permite a individuos, empresas, universidades y todo tipo de organizaciones de todo el mundo aumentar sus habilidades de hacking. \n\nPagina web oficial:\nwww.hackthebox.com",
    "htb":"Hack The Box \n\nEs una plataforma masiva de capacitación en ciberseguridad en línea, que permite a individuos, empresas, universidades y todo tipo de organizaciones de todo el mundo aumentar sus habilidades de hacking. \n\nPagina web oficial:\nwww.hackthebox.com",
    "oscp": "Certificado profesional en seguridad ofensiva \n\nEs una certificación de ethical hacking ofrecida por Offensive Security que enseña metodologías de exámenes de penetración y utiliza herramientas que incluyen el examen de pentración BackTrack \n\nMas informacion: \nwww.offensive-security.com/pwk-oscp",
    "ctf":"Capture The Flag\n\nUn CTF (Capture The Flag) en Español, «Captura la bandera». Son competiciones que nos permiten poner a prueba nuestras habilidades sobre hacking por medio de retos de diferentes modalidades que tendremos que resolver para conseguir el premio, la famosa «flag». Las banderas se colocan en varias ubicaciones, pueden estar en un archivo, en la base de datos, pegadas en el código fuente o de otra manera, y su objetivo es buscarlas todas.",
    "capture the flag":"Capture The Flag\n\nUn CTF (Capture The Flag) en Español, «Captura la bandera». Son competiciones que nos permiten poner a prueba nuestras habilidades sobre hacking por medio de retos de diferentes modalidades que tendremos que resolver para conseguir el premio, la famosa «flag». Las banderas se colocan en varias ubicaciones, pueden estar en un archivo, en la base de datos, pegadas en el código fuente o de otra manera, y su objetivo es buscarlas todas.",
    "captura la bandera":"Capture The Flag\n\nUn CTF (Capture The Flag) en Español, «Captura la bandera». Son competiciones que nos permiten poner a prueba nuestras habilidades sobre hacking por medio de retos de diferentes modalidades que tendremos que resolver para conseguir el premio, la famosa «flag». Las banderas se colocan en varias ubicaciones, pueden estar en un archivo, en la base de datos, pegadas en el código fuente o de otra manera, y su objetivo es buscarlas todas.",
    "narnia":"Narnia\n\nNarnia es sitio desconocido, pocos humanos han podido encontrarlo y aun esta en duda su existencia, solo se sabe que es un sitio oscuro, solitario, frio y no debe confundirse con un cuento de fantacia llamado 'las cronicas de narnia' \n\nMas informacion: \nGoogle Maps",
    "thm":"TryHackMe\n\nEs una plataforma web en la que podremos aprender hacking desde 0, a base de resolver retos con una filosofía de CTF y gamificación.",
    "try hack me":"TryHackMe\n\nEs una plataforma web en la que podremos aprender hacking desde 0, a base de resolver retos con una filosofía de CTF y gamificación.",
    "hacking":"Hacking\n\nLa búsqueda permanente de conocimientos en todo lo relacionado con sistemas informáticos, sus mecanismos de seguridad, las vulnerabilidades de los mismos, la forma de aprovechar estas vulnerabilidades y los mecanismos para protegerse de aquellos que saben hacerlo",
    "pentesting":"Pentesting\n\nLa acción o la actividad de atacar un sistema informático para identificar fallos, vulnerabilidades y demás errores de seguridad existentes, para así poder prevenir los ataques externos. Además, el pentesting realmente es una forma de hacking, solo que esta práctica es totalmente legal, ya que cuenta con el consentimiento de los propietarios de los equipos que se van a testear, además de tener la intención de causar un daño real",
    "penetration testing":"Pentesting\n\nLa acción o la actividad de atacar un sistema informático para identificar fallos, vulnerabilidades y demás errores de seguridad existentes, para así poder prevenir los ataques externos. Además, el pentesting realmente es una forma de hacking, solo que esta práctica es totalmente legal, ya que cuenta con el consentimiento de los propietarios de los equipos que se van a testear, además de tener la intención de causar un daño real",
    "pentester":"Pentester\n\nCuyo trabajo consiste en seguir varios procesos o pasos determinados que garanticen un buen examen y que pueda realizar así todas las averiguaciones posibles sobre fallos o vulnerabilidades en el sistema. Por lo que, muchas veces es llamado Auditor de Ciberseguridad",
    "blackhat":"Hacker de sombrero negro\n\nUn hacker de sombrero negro (o cracker) es un hacker que viola la seguridad por razones mas allá de la malicia o para beneficio personal. Los hackers de sobrero negro son la personificación de todo lo que el publico teme de un criminal informático. Pueden atacar en grupo, trabajar para algún gobierno/empresa o independientemente.",
    "black hat":"Hacker de sombrero negro\n\nUn hacker de sombrero negro (o cracker) es un hacker que viola la seguridad por razones mas allá de la malicia o para beneficio personal. Los hackers de sobrero negro son la personificación de todo lo que el publico teme de un criminal informático. Pueden atacar en grupo, trabajar para algún gobierno/empresa o independientemente.",
    "hacker sombrero negro":"Hacker de sombrero negro\n\nUn hacker de sombrero negro (o cracker) es un hacker que viola la seguridad por razones mas allá de la malicia o para beneficio personal. Los hackers de sobrero negro son la personificación de todo lo que el publico teme de un criminal informático. Pueden atacar en grupo, trabajar para algún gobierno/empresa o independientemente.",
    "whitehat":"Hacker de sombrero blanco\n\nUn hacker de sombrero blanco es un hacker ético o experto en seguridad informática quien se especializa en pruebas de penetración y en otras metodologías para detectar vulnerabilidades y mejorar la seguridad de los sistemas de comunicación e información en una organización.",
    "hacker de sombrero negro":"Hacker de sombrero negro\n\nUn hacker de sombrero negro (o cracker) es un hacker que viola la seguridad por razones mas allá de la malicia o para beneficio personal. Los hackers de sobrero negro son la personificación de todo lo que el publico teme de un criminal informático. Pueden atacar en grupo, trabajar para algún gobierno/empresa o independientemente.",
    "white hat":"Hacker de sombrero blanco\n\nUn hacker de sombrero blanco es un hacker ético o experto en seguridad informática quien se especializa en pruebas de penetración y en otras metodologías para detectar vulnerabilidades y mejorar la seguridad de los sistemas de comunicación e información en una organización.",
    "hacker sombrero blanco":"Hacker de sombrero blanco\n\nUn hacker de sombrero blanco es un hacker ético o experto en seguridad informática quien se especializa en pruebas de penetración y en otras metodologías para detectar vulnerabilidades y mejorar la seguridad de los sistemas de comunicación e información en una organización.",
    "hacker de sombrero blanco":"Hacker de sombrero blanco\n\nUn hacker de sombrero blanco es un hacker ético o experto en seguridad informática quien se especializa en pruebas de penetración y en otras metodologías para detectar vulnerabilidades y mejorar la seguridad de los sistemas de comunicación e información en una organización.",
    "django":"Django \n\nEs un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como modelo-vista-controlador (MVC).",
    "webscraping":"Web scraping o raspado web \n\nEs una técnica utilizada mediante programas de software para extraer información de sitios web.​ Usualmente, estos programas simulan la navegación de un humano en la World Wide Web ya sea utilizando el protocolo HTTP manualmente, o incrustando un navegador en una aplicación."
    }

    if palabra in definiciones.keys():
        return definiciones[palabra]
    else:
        import wikipedia
        wikipedia.set_lang("es")
     
        try: 
            resumen = wikipedia.summary(palabra, sentences = 1)
            url = (wikipedia.page(palabra).url)
            resultado = (resumen + "\n\nMas info: " + url)
            return resultado
        except: 
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