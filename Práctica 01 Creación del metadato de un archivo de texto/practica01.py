# instalacion librerias en comandos
    #pip install nltk - linea de comandos
    #python -m nltk.downloader all

# re libreria de expresiones regulares
import re
import string
# verificar si es un archivo
import os.path

# libreria de palabras nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Metodo para quitar signos de puntuación


def remove_punctuation(text):
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    return re.sub('[%s]' % re.escape('“”¬¿¡°´'), '', text)

# Metodo para quitar numeros


def remove_numeros(text):
    return re.sub('[%s]' % re.escape('0123456789'), '', text)

# Metodo para Quitamos acentos


def remove_acentos(text):
    text = re.sub('[%s]' % re.escape('á'), 'a', text)
    text = re.sub('[%s]' % re.escape('é'), 'e', text)
    text = re.sub('[%s]' % re.escape('í'), 'i', text)
    text = re.sub('[%s]' % re.escape('ó'), 'o', text)
    text = re.sub('[%s]' % re.escape('ü'), 'u', text)
    return re.sub('[%s]' % re.escape('ú'), 'u', text)

# Metodo para Quitar los adjetivos


def remove_adjetivos(palabras):
    adjetivos = ['afortunado', 'diligente', 'negro', 'alto', 'directo', 'anaranjado', 'anormal', 'dos', 'nueve', 'amable', 'duro', 'obsecuente', 'antiguo', 'el', 'ocho', 'amarillo',
                 'enorme', 'paciente', 'angosto', 'estupendo', 'pequeño', 'aquel', 'extremo', 'popular', 'argentino', 'facil', 'primer', 'azul', 'famoso', 'querido', 'bajisimo',
                 'flexible', 'quinto', 'bajo', 'generosos', 'redonda', 'blanco', 'grande', 'rigido', 'blando', 'gris', 'rojo', 'brillante', 'honesto', 'segundo', 'bruto', 'incomodas',
                 'seis', 'buena', 'increible', 'sencillo', 'bueno', 'indirecto', 'septimo', 'chileno', 'inepto', 'sexto', 'cinco', 'inexpresiva', 'siete', 'complejo', 'infeliz', 'simple',
                 'complicado', 'inobjetable', 'sincero', 'conocido', 'inoperante', 'soberbio', 'cualquier', 'insatisfecho', 'tercero', 'cuarto', 'inteligente', 'tres', 'la', 'tu', 'las',
                 'una', 'desafortunado', 'los', 'uno', 'desconocido', 'magnifico', 'uruguayo', 'deshonesto', 'mala', 'verde', 'deteriorado', 'malo', 'violeta', 'diez', 'marginado',
                 'voluptuoso', 'dificil', 'mayor', 'vuestro', 'mi', 'mis', 'mio', 'mia', 'mias', 'tus', 'tuyo', 'tuyos', 'tuya', 'tuyas', 'su', 'sus', 'suyo', 'suyos', 'suya', 'suyas',
                 'nuestro', 'nuestros', 'nuestra', 'nuestras', 'vuestros', 'vuestras', 'esa', 'este', 'esas', 'estos', 'ese', 'esos', 'aquella', 'esta', 'aquellos', 'estas', 'aquellas',
                 'cien', 'doscientos', 'trescientos', 'cuatro', 'veinte', 'treinta', 'mil', 'cuarenta', 'cincuenta', 'un', 'millon', 'primero', 'octavo', 'veinteavo', 'noveno', 'tercer',
                 'decimo', 'treintavo', 'cuarentavo', 'cincuentavo', 'ultimo', 'doble', 'cuadruple', 'sextuple', 'triple', 'quintuple', 'octuple', 'medio', 'tercio', 'algun', 'demas',
                 'tantos', 'alguno', 'demasiados', 'todos', 'algunos', 'escasos', 'ambos', 'muchos', 'unas', 'bastantes', 'ninguno', 'cada', 'otros', 'cierto', 'pocos', 'unos',
                 'cualquiera', 'tal', 'varios', 'veinticincoavo', 'veintiseisavo', 'veintisieteavo', 'veintiochoavo', 'veintinueveavo', 'trigesimo', 'trigesima', 'cuadragesimo',
                 'cuadragesima', 'sesentavo', 'sexagesimo', 'undecimo', 'onceavo', 'setentavo', 'septuagesimo', 'duodecimo', 'doceavo', 'ochentavo', 'octogesimo', 'treceavo',
                 'noventavo,', 'nonagesimo', 'catorceavo', 'centavo,', 'centesimo', 'quinceavo', 'ducentesimo', 'dieciseisavo', 'tricentesimo', 'diecisieteavo', 'cuadringentesimo',
                 'dieciochoavo', 'diezmilesimo', 'diecinueveavo', 'cienmilesimo', 'vigesimo', 'millonesimo', 'veintiunavo', 'diezmillonesimo', 'veintidosavo', 'cienmillonesimo',
                 'veintitresavo', 'milmillonesimo', 'veinticuatroavo', 'billonesimo', 'del', 'lo', 'al', 'simpatico', 'lento', 'rigidos', 'simnple', 'tenebrosa', 'habil', 'limpio',
                 'fuerte', 'especial', 'impulsivo', 'intrepida', 'ansioso', 'redondo', 'moderno', 'ruidoso', 'pequeña', 'delgada', 'irresponsable', 'maduro', 'enfermo', 'grandes',
                 'curioso', 'nueva', 'cordial', 'sutil', 'monotonos', 'amarillento', 'estudioso', 'modesto', 'entrometida', 'vulgar', 'feliz', 'feo', 'antiguos', 'simples',
                 'extraordinario', 'imperfecto', 'inteligentes', 'generoso', 'maravilloso', 'fria', 'ardiente', 'distante', 'sensibles', 'apasionado', 'mediano', 'nuevo', 'ansiada',
                 'colorido', 'odioso', 'cuidadoso', 'blanca', 'ambicioso', 'arrugado', 'bellos', 'viejo', 'sencillos', 'agradable', 'gordo', 'dura', 'desordenado', 'horrible', 'prolijo',
                 'pacifico', 'rosado', 'refinado', 'acida', 'celoso', 'alargado', 'angelical', 'estresante', 'contento', 'sucio', 'valiente', 'enfermiza', 'lindo', 'transparente', 'flaco',
                 'fragil', 'incomoda', 'diferente', 'triste', 'corto', 'fugaz', 'crocante', 'engreidas', 'ancha', 'debil', 'libre', 'timida', 'caliente', 'agotador', 'complicados',
                 'calido', 'desconfiado', 'quebrado', 'bonito', 'realista', 'suave', 'complejos', 'chiquito', 'azulado', 'cansado', 'marron', 'peludo', 'cuadrado', 'apatico', 'luminoso',
                 'coherente', 'helado', 'interesante', 'aburrido', 'cultos', 'atento', 'alegres', 'cauto', 'afectuoso', 'insensible', 'inmensas', 'malcriado', 'grueso', 'agil', 'dulce',
                 'burlon', 'ordenado', 'celeste', 'comodo', 'abstracto', 'considerado', 'rapido', 'sobrio', 'negra', 'cruel', 'largo', 'ancho', 'amargado', 'perfecto', 'extrovertida',
                 'infantil', 'mas']
    return [palabra for palabra in palabras if not palabra in adjetivos]

# Metodo para quitar adverbios


def remove_adverbios(tokens):
    lugar = ['traves', 'aqui', 'donde', 'abajo', 'arriba', 'en', 'aca', 'atras', 'encima', 'afuera', 'bajo', 'enfrente', 'ahi', 'cerca',
             'entre', 'borde', 'delante', 'junto', 'a', 'alla', 'dentro', 'lejos', 'allí', 'desde', 'debajo', 'alrededor', 'detras', 'sobre']
    palabras = [palabra for palabra in tokens if not palabra in lugar]

    tiempo = ['actualmente', 'enseguida', 'normalmente', 'ahora', 'entretanto', 'nunca', 'anoche', 'eternamente', 'ocasionalmente', 'anteriormente', 'finalmente', 'posteriormente', 'antes', 'frecuentemente', 'primeramente', 'antiguamente', 'hoy', 'pronto', 'asiduamente', 'inicialmente',
              'puntualmente', 'aun', 'inmediatamente', 'recien', 'ayer', 'instantaneamente', 'recientemente', 'constantemente', 'jamas', 'siempre', 'contemporaneamente', 'luego', 'simultaneamente', 'cuando', 'mañana', 'tarde', 'desde', 'mientras', 'temprano', 'despues', 'momentaneamente', 'ya']
    palabras = [palabra for palabra in palabras if not palabra in tiempo]

    modo = ['adrede', 'fuertemente', 'publicamente', 'amable', 'fuerte', 'puntillosamente', 'apasionadamente', 'gratuitamente', 'rapidamente', 'asi', 'habilmente', 'rapido', 'asiduamente', 'igual', 'regular', 'bajo', 'igualmente', 'responsablemente', 'bien', 'inocentemente', 'rutinariamente', 'brillantemente', 'intelectualmente', 'salvajemente', 'claro', 'lentamente',
            'suavemente', 'conforme', 'lento', 'subitamente', 'debilmente', 'ligero', 'sutilmente', 'desgraciadamente', 'mal', 'talentosamente', 'elegantemente', 'mejor', 'tiernamente', 'elocuentemente', 'minuciosamente', 'tiernamente', 'espontaneamente', 'nuevamente', 'velozmente', 'facilmente', 'oportunamente', 'voluntariamente', 'formalmente', 'prolijamente', 'vulgarmente']
    palabras = [palabra for palabra in palabras if not palabra in modo]

    cantidad = ['demasiado', 'mitad', 'solo', 'suficientemente', 'apenas', 'mucho', 'extremadamente', 'bastante', 'muy',
                'tan', 'excesivamente', 'casi', 'nada', 'tanto', 'absolutamente', 'justo', 'poco', 'todo', 'aproximadamente']
    palabras = [palabra for palabra in palabras if not palabra in cantidad]

    negacion = ['no', 'nunca', 'jamas', 'nada', 'ni', 'siquiera',
                'ningún', 'nunca', 'tampoco', 'ninguno', 'jamas', 'nadie', 'ninguna']
    palabras = [palabra for palabra in palabras if not palabra in negacion]

    afirmacion = ['si', 'desde', 'efectivamente', 'indiscutiblemente',
                  'obviamente', 'seguramente', 'tambien', 'verdaderamente', 'obvio']
    palabras = [palabra for palabra in palabras if not palabra in afirmacion]

    duda = ['posiblemente', 'acaso', 'quiza', 'probablemente', 'quizas', 'seguramente', 'aparentemente', 'eventualmente',
            'indudablemente', 'definitivamente', 'parecer', 'mejor', 'ahi', 'tal', 'vez', 'seguro', 'casi', 'mejor', 'quien', 'sabe']
    palabras = [palabra for palabra in palabras if not palabra in duda]

    return palabras

# Metodo para quitar verbos


def remove_verbos(tokens):
    nuevo = []
    for palabra in tokens:
        if(palabra[-5:] == "yendo" or palabra[-4:] == "ando" or palabra[-4:] == "endo" or (palabra[-2:] == "ar" and palabra != "mar") or (palabra[-2:] == "er" and palabra != "ser") or palabra[-2:] == "ir" or palabra[-2:] == "ia" or palabra[-3:] == "ias" or palabra[-5:] == "iamos" or palabra[-3:] == "ian" or palabra[-2:] == "io" or palabra[-4:] == "iste" or palabra[-3:] == "ire" or palabra[-4:] == "iras" or palabra[-3:] == "ira" or palabra[-6:] == "iremos" or palabra[-4:] == "iran" or palabra[-4:] == "amos" or palabra[-4:] == "emos" or palabra[-4:] == "imos" or palabra[-5:] == "abamos" or palabra[-4:] == "aban"):
            print("Procesando...")
        else:
            nuevo.append(palabra)
    return nuevo


# Pedimos el nombre del archivo
archivo = input("Ingresa la dirección completa del archivo de texto: ")

# Verificamos si es un archivo
if os.path.isfile(archivo):
    # Abrimos el archivo de texto y extraemos su contenido
    with open(archivo, "r", encoding="utf-8") as archivoMemoria:
        texto = archivoMemoria.read()

    # Depuramos el texto
    # Hacemos minusculas todo el texto
    texto = texto.lower()
    # Quitamos los acentos
    texto = remove_acentos(texto)
    # Signos de puntuacion y caracteres especiales
    texto = remove_punctuation(texto)
    # Quitamos numeros
    texto = remove_numeros(texto)

    # Dividir las palabras
    palabras = word_tokenize(texto)

    # Quitar palabras de parada (Artículos, Pronombres, Preposiciones, Conjunciones)
    palabrasParada = stopwords.words('spanish')
    palabras = [palabra for palabra in palabras if not palabra in palabrasParada]

    # Quitar Adjetivos
    palabras = remove_adjetivos(palabras)

    # Quitar Adverbios
    palabras = remove_adverbios(palabras)

    # Quitar Verbos
    palabras = remove_verbos(palabras)

    # Contar palabras
    palabrasBuscar = []
    for palabra in palabras:
        if not palabra in palabrasBuscar:
            palabrasBuscar.append(palabra)
    repeticiones = []
    for palabra in palabrasBuscar:
        repeticiones.append(palabras.count(palabra))

    # Mostrar las palabras repetidas
    listaRepeticiones = sorted(
        list(zip(palabrasBuscar, repeticiones)), key=lambda x: x[1], reverse=True)
    print("--------------------------------------------------------------------------------------------------")
    print("Palabras que mas se repiten")
    print("--------------------------------------------------------------------------------------------------")
    for elemento in listaRepeticiones[0:3]:
        print(elemento[0])
else:
    print("La dirección dada no es un archivo")
