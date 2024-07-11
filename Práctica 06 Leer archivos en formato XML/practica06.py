#Práctica 6: Leer archivos en formato XML
#Windows 10
#Python 3.8.6
#-------------------------------------------
# Libreria de requests => pip install requests
# Libreria Beautifulsoup => pip install beautifulsoup4
# lxl => pip3 install lxml
#-------------------------------------------

import requests
import lxml
from bs4 import BeautifulSoup

#Lista de palabras
listaBuenas = ['like','start', 'excitement', 'peace', 'love', 'powerful', 'mindful', 'strong', 'motivation', 'encouragement', 'kindness', 'empowerment', 'resourceful', 'meditative', 'growth', 'satisfaction', 'help', 'achievement', 'gratitude', 'confidence', 'clarity', 'happy', 'successful', 'resilient', 'progress', 'accomplishment', 'appreciation', 'energy', 'gain', 'joy', 'advantage', 'inspiration', 'anticipation', 'creativity', 'imagination', 'comfort', 'playful', 'dream', 'productive', 'adaptability', 'skilful', 'problemsolving', 'cooperative', 'fun', 'enjoyment', 'savor', 'sunshine', 'hopeful', 'healthy', 'grateful', 'optimistic', 'spiritual', 'exercise', 'relaxation', 'friendliness', 'beauty', 'nature', 'positive', 'enough', 'exhilaration', 'exceptional', 'profit', 'peaceful', 'giving', 'shine', 'contentment', 'advance', 'flourish', 'calm', 'declutter', 'improve', 'adventurous', 'lively', 'safe', 'laughter', 'agreement', 'compassion', 'believe', 'freedom', 'understanding', 'excellent', 'selfbelief', 'flexibility', 'surpass', 'stable', 'present', 'focused', 'goaloriented', 'celebrating', 'community', 'gracious', 'sharing', 'conviviality', 'space', 'serenity', 'trust', 'openness', 'opportunity', 'clearheadedness', 'brighten', 'terrific', 'wellbeing', 'nourishment', 'selfcare', 'transformation', 'cheerful', 'fulfilment', 'flow', 'interesting', 'sincere', 'fantastic', 'wise', 'allencompassing', 'tranquillity', 'vision', 'fabulous', 'absorbing', 'vitality', 'courage', 'unique', 'action', 'better', 'smile', 'illuminate', 'winwin', 'spunky', 'best', 'sanctuary', 'selfesteem', 'selfconfidence', 'value', 'capable', 'happiness', 'commitment', 'consistency', 'patience', 'invigorated', 'benefit', 'new', 'imagine', 'create', 'empathy', 'active', 'generous', 'share', 'light', 'engagement', 'challenge', 'listen', 'honor', 'pleasure', 'truthful', 'enthusiastic', 'radiant', 'committed', 'facilitate', 'faithful', 'purpose', 'acceptance', 'learn', 'innovative', 'solutionsoriented', 'togetherness', 'original', 'energetic', 'growing', 'useful', 'splendid', 'enhance', 'plenty', 'quality', 'remarkable', 'caring', 'glad', 'begin', 'persistence', 'thrive', 'invincible', 'brave', 'free', 'good', 'solid', 'heal', 'brilliant', 'integrity', 'selfmastery', 'mediate', 'rest', 'concentrate', 'support', 'perspective', 'pleasant', 'connect', 'helpful', 'interest', 'curiosity', 'vivacious', 'interact', 'awareness', 'fascinating', 'valuable', 'reassure', 'breathe', 'compassionate', 'wisdom', 'limitless', 'soul', 'surrender', 'wonder', 'express', 'organized', 'passion', 'humor', 'stillness', 'faith', 'balance', 'genuine', 'ease', 'abundance', 'reward', 'open', 'delight', 'profitable', 'versatile', 'delicious', 'worthy', 'centered', 'joyful', 'honest', 'affirmation', 'yes', 'choice', 'selfmotivation', 'impressive', 'authentic', 'intuition', 'harmony', 'insightful', 'optimal', 'perceptive', 'adept', 'intention', 'worthwhile', 'forgive', 'richness', 'energized', 'rejoice', 'applaud', 'simplicity', 'nonjudgmental', 'effortless', 'move', 'inspire', 'boost', 'embolden', 'stunning', 'animated', 'supportive', 'nurture', 'invent', 'spectacular', 'extend', 'thankful', 'assistance', 'uplift', 'elated', 'meaningful', 'thrilled', 'lighthearted', 'gleam', 'alive', 'treasure', 'bliss', 'upbeat', 'cando', 'efficient', 'loving', 'eager', 'keen', 'gogetting', 'guiltfree', 'wonderful', 'ingenious', 'solution', 'delightful', 'incredible', 'divine', 'harmonious', 'generous', 'amazing', 'magnificent', 'great', 'vibrant', 'affirmative', 'conscious', 'empathetic', 'engaging', 'refreshing', 'sparkling', 'stupendous', 'well', 'fearless', 'inclusive', 'vitality', 'sustain', 'reinforce', 'competent', 'tenacious', 'solve', 'profound', 'depth', 'healing', 'presence', 'glow', 'ingenuity', 'donate', 'satisfied', 'determined', 'grounded', 'spirited', 'forward', 'climb', 'empower', 'silence', 'thanks', 'blessing', 'awesome', 'change', 'soulful', 'individuality', 'expand', 'forge', 'goal', 'liberty', 'friendship', 'extraordinary', 'care', 'volunteer', 'discover', 'choose', 'being', 'stretch', 'rainbow', 'miracle', 'responsibility', 'respect', 'respond', 'welcome', 'comfortable', 'allow', 'recover', 'revitalize', 'strengthen', 'littlebylittle', 'nourish', 'secure', 'give', 'transform', 'openhearted', 'forwardlooking', 'restorative', 'thoughtful', 'serendipity', 'amusement', 'relinquish', 'magnanimous', 'spontaneous']
listaMalas = ['abysmal', 'adverse', 'alarming', 'angry', 'annoy', 'anxious', 'apathy', 'appalling', 'atrocious', 'awful', 'bad', 'banal', 'barbed', 'belligerent', 'bemoan', 'beneath', 'boring', 'broken', 'callous', 'cant', 'clumsy', 'coarse', 'cold', 'coldhearted', 'collapse', 'confused', 'contradictory', 'contrary', 'corrosive', 'corrupt', 'crazy', 'creepy', 'criminal', 'cruel', 'cry', 'cutting', 'damage', 'damaging', 'dastardly', 'dead', 'decaying', 'deformed', 'deny', 'deplorable', 'depressed', 'deprived', 'despicable', 'detrimental', 'dirty', 'disease', 'disgusting', 'disheveled', 'dishonest', 'dishonorable', 'dismal', 'distress', 'dont', 'dreadful', 'dreary', 'enraged', 'eroding', 'evil', 'fail', 'faulty', 'fear', 'feeble', 'fight', 'filthy', 'foul', 'frighten', 'frightful', 'gawky', 'ghastly', 'grave', 'greed', 'grim', 'grimace', 'gross', 'grotesque', 'gruesome', 'guilty', 'haggard', 'hard', 'hardhearted', 'harmful', 'hate', 'hideous', 'homely', 'horrendous', 'horrible', 'hostile', 'hurt', 'hurtful', 'icky', 'ignorant', 'ignore', 'ill', 'immature', 'imperfect', 'impossible', 'inane', 'inelegant', 'infernal', 'injure', 'injurious', 'insane', 'insidious', 'insipid', 'jealous', 'junky', 'lose', 'lousy', 'lumpy', 'malicious', 'mean', 'menacing', 'messy', 'misshapen', 'missing', 'misunderstood', 'moan', 'moldy', 'monstrous', 'naive', 'nasty', 'naughty', 'negate', 'negative', 'never', 'no', 'nobody', 'nondescript', 'nonsense', 'not', 'noxious', 'objectionable', 'odious', 'offensive', 'old', 'oppressive', 'pain', 'perturb', 'pessimistic', 'petty', 'plain', 'poisonous', 'poor', 'prejudice', 'questionable', 'quirky', 'quit', 'reject', 'renege', 'repellant', 'reptilian', 'repugnant', 'repulsive', 'revenge', 'revolting', 'rocky', 'rotten', 'rude', 'ruthless', 'sad', 'savage', 'scare', 'scary', 'scream', 'severe', 'shocking', 'shoddy', 'sick', 'sickening', 'sinister', 'slimy', 'smelly', 'sobbing', 'sorry', 'spiteful', 'sticky', 'stinky', 'stormy', 'stressful', 'stuck', 'stupid', 'substandard', 'suspect', 'suspicious', 'tense', 'terrible', 'terrifying', 'threatening', 'ugly', 'undermine', 'unfair', 'unfavorable', 'unhappy', 'unhealthy', 'unjust', 'unlucky', 'unpleasant', 'unsatisfactory', 'unsightly', 'untoward', 'unwanted', 'unwelcome', 'unwholesome', 'unwieldy', 'unwise', 'upset', 'vice', 'vicious', 'vile', 'villainous', 'vindictive', 'wary', 'weary', 'wicked', 'woeful', 'worthless', 'wound', 'yell', 'yucky', 'zero', 'no', 'not', 'none', 'noone', 'nobody', 'nothing', 'neither', 'nowhere', 'never', 'hardly', 'scarcely', 'barely', 'doesnt', 'isnt', 'wasnt', 'shouldnt', 'wouldnt', 'couldnt', 'wont', 'cant', 'dont']

#Quitar caracteres
def quitarCaracteres(cadena):
    nueva = ""
    for caracter in cadena:
        if caracter.isalpha() or caracter == ' ':
            nueva+=caracter
    return nueva.lower()

#Leer el archivo XML
urlXML = "https://itunes.apple.com/us/rss/customerreviews/page=1/id=284882215/sortBy=mostrecent/xml"
print("LEYENDO DEL ARCHIVO XML => "+urlXML)
texto = requests.get(urlXML).content

#Dar formato al XML
datos = BeautifulSoup(texto, "lxml")

#Obtener los comentarios
print("Opteniendo comentarios . . .")
comentariosXML = datos.find_all("content")
i = 0
comentarios = []
for comentario in comentariosXML:
    if (i % 2) == 0:
        comentarios.append(quitarCaracteres(comentario.text))
    i+=1
print("Numero de comentarios: "+str(len(comentarios)))

#Parseando por palabras por espacio
comentariosPalabras = []
for comentario in comentarios:
    comentariosPalabras.append(str(comentario).split())

#Clasifiacando comentarios
print("Clasificando comentarios . . .")
i = 0
comentarioBueno = []
comentarioMalo = []
for comentario in comentariosPalabras:
    contBuenas = 0
    contMalas = 0
    for palabra in comentario:
        if palabra in listaBuenas:
            contBuenas += 1
        if palabra in listaMalas:
            contMalas += 1
    if contBuenas > contMalas:
        comentarioBueno.append(comentarios[i])
    elif contBuenas < contMalas:
        comentarioMalo.append(comentarios[i])
    i+=1

#Imprimir resultado
print("----------------------------------------------------------------------------------------------")
print("COMENTARIOS POSITIVOS")
for comentario in comentarioBueno[0:3]:
    print(comentario+'\n')
print("----------------------------------------------------------------------------------------------")
print("COMENTARIOS NEGATIVOS")
for comentario in comentarioMalo[0:3]:
    print(comentario+'\n')
print("----------------------------------------------------------------------------------------------")

