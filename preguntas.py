data = [
    {'respuesta': 'Hola', 
        "palabras": ['hola', 'klk', 'saludos', 'buenas'], 
        "single_response" : True, 
        "required_words":[]},

    {'respuesta': 'Desarrollo de software',
        "palabras":['cual', 'carrera', 'estudiantes'],
        "single_response":True,
        "required_words":['mas']},

    {'respuesta': 'En el ano 2000', 
        "palabras":['cuando', 'itla', 'año', 'se creo'],
        "single_response":True,
        "required_words":[]},

    {'respuesta': """Las carreras que impartimos son: 
                     SIMULACIONES INTERACTIVAS Y VIDEOJUEGOS
                     TELECOMUNICACIONES
                     INTELIGENCIA ARTIFICIAL
                     INFORMÁTICA FORENSE
                     ENERGÍAS RENOVABLES
                     REDES DE INFORMACIÓN
                     MECATRÓNICA
                     MANUFACTURA AUTOMATIZADA
                     MANUFACTURA DE DISPOSITIVOS MÉDICOS
                     DISEÑO INDUSTRIAL
                     MULTIMEDIA
                     SONIDO
                     DESARROLLO DE SOFTWARE
                     ANALÍTICA Y CIENCIA DE LOS DATOS
                     SEGURIDAD INFORMÁTICA
                 """,
            "palabras":['cuales', 'carreras', 'imparten'],
            "single_response":False,
            "required_words":['carreras']},

    {'respuesta': 'estamos ubicados en Las Américas Highway, Km. 27, La Caleta',
        "palabras":['ubicados', 'direccion', 'donde', 'ubicacion'],
        "single_response":False,
        "required_words":['santo','domingo']},

    {'respuesta': 'En santiago estamos en Edificio Metropolitano I, Segundo Nivel, Av. 27 de Febrero',
        "palabras":['ubicados', 'direccion', 'donde', 'ubicacion'],
        "single_response":False,
        'required_words':['santiago']},

    {'respuesta': '2 años y 4 meses', "palabras":['duracion', 'dura', 'cual', 'carreras'],
        "single_response":False,
        "required_words":['carreras', 'duracion']},

    {'respuesta': 'Accediendo a este enlace: https://plataformavirtual.itla.edu.do/',
        "palabras":['link', 'enlace', 'plataforma', 'virtual', 'cual'],
        "single_response":True,
        "required_words":['plataforma']},

    {'respuesta': 'accediendo al siguiente enlace con su usuario y contrasena: https://orbi.edu.do/orbi/',
        "palabras":['ver calificacion', 'donde', 'ver', 'calificacion'],
        "single_response":False,
        "required_words":['calificaciones']
    },
    {'respuesta': 'Si, si tiene cancha',
        "palabras":['cancha', 'basketball', 'itla'],
        "single_response":True,
        "required_words":['basketball']
    }]
