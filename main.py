import re
import random
import preguntas

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        
        for i in range(len(preguntas.data)):
            response(preguntas.data[i]['respuesta'], preguntas.data[i]['palabras'], required_words=preguntas.data[i]['required_words'])
    
        # for i in range(len(data)):
        #     data[i]["respuesta"]

        # response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        
        # response('Desarrollo de software', ['cual', 'carrera', 'con mas estudiantes'], single_response=True)
        
        # response('En el ano 2000', ['cuando', 'itla', 'año', 'se creo'], single_response=True)
        # response("""Las carreras que impartimos son: 
        #             SIMULACIONES INTERACTIVAS Y VIDEOJUEGOS
        #             TELECOMUNICACIONES
        #             INTELIGENCIA ARTIFICIAL
        #             INFORMÁTICA FORENSE
        #             ENERGÍAS RENOVABLES
        #             REDES DE INFORMACIÓN
        #             MECATRÓNICA
        #             MANUFACTURA AUTOMATIZADA
        #             MANUFACTURA DE DISPOSITIVOS MÉDICOS
        #             DISEÑO INDUSTRIAL
        #             MULTIMEDIA
        #             SONIDO
        #             DESARROLLO DE SOFTWARE
        #             ANALÍTICA Y CIENCIA DE LOS DATOS
        #             SEGURIDAD INFORMÁTICA
        #         """, ['cuales', 'carreras', 'imparten'], required_words=['carreras'])
        
        # response('estamos ubicados en Las Américas Highway, Km. 27, La Caleta', ['ubicados', 'direccion', 'donde', 'ubicacion'], required_words=['santo','domingo'])
        # response('En santiago estamos en Edificio Metropolitano I, Segundo Nivel, Av. 27 de Febrero',
        # ['ubicados', 'direccion', 'donde', 'ubicacion'], required_words=['santiago'])
        # response('2 años y 4 meses', ['duracion', 'dura', 'cual', 'carreras'], required_words=['carreras', 'duracion'])
        # response('Accediendo a este enlace: https://plataformavirtual.itla.edu.do/', ['link', 'enlace', 'plataforma', 'virtual', 'cual'], single_response=True)
        # response('accediendo al sigueinte enlace con su usuario y contrasena: https://orbi.edu.do/orbi/', ['ver calificacion', 'donde', 'ver', 'calificacion'], required_words=['calificaciones'])

        best_match = max(highest_prob, key=highest_prob.get)

        return unknown() if highest_prob[best_match] < 1 else best_match

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))