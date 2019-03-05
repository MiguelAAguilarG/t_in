import random
import os

'''
https://www.shertonenglish.com/es/gramatica/voz-activa-en-ingles
present simple
present continuous
present perfect
present perfect continuous

past simple
past continuous
past perfect
past perfect continuous

future simple
future continuous
future perfect
future perfect continuous

future -be going to- simple
future -be going to- continuous
future -be going to- perfect
future -be going to- perfect continuous

future -be going to- paast simple
future -be going to- paast continuous
future -be going to- paast perfect
future -be going to- paast perfect continuous

conditional
conditional continuous
conditional perfect
conditional perfect continuous
'''

subjects_pronouns_list_1 = ['I ']
subjects_pronouns_list_2 = ['you ']
subjects_pronouns_list_3 = ['he ','she ', 'it ']
subjects_pronouns_list_4 = ['we ','they ']

subjects_pronouns_list = subjects_pronouns_list_1 + subjects_pronouns_list_2 + subjects_pronouns_list_3 + subjects_pronouns_list_4
subjects_pronouns_list_singular = subjects_pronouns_list_1 + subjects_pronouns_list_2 + subjects_pronouns_list_3
subjects_pronouns_list_plural = subjects_pronouns_list_2 + subjects_pronouns_list_4
###########################################################
tenses_list = ['past', 'present', 'future','future -be going to-','future -be going to- past', 'conditional']
types_list = ['simple','continuous/progressive','perfect','perfect continuous/progressive']
###########################################################
verbs_to_be = ['am ','are ','is ']
verbs_to_be_past = ['was ','were ']

verbs_to_have = ['have ','has ']
verbs_to_have_past = ['had ']

verbs_to_do = ['do ','does ']
verbs_to_do_past = ['did ']

auxiliar_not = ['not ']
auxiliar_would = ['would ']
###########################################################
verbs_regular = ['abandon', 'absolve', 'abuse', 
'accelerate', 'accept', 'accustom', 'acquire', 
'add', 'admire', 'adore', 'advance', 'advise', 'agree', 
'amount', 'announce', 'answer', 'appear', 'approach', 
'arrange', 'ask', 'astonish', 'attempt', 'attract', 'bathe',
'believe', 'blame', 'call', 'cash', 'change', 'claim', 
'clear', 'close', 'comb', 'command', 'compare', 'compose', 
'consider', 'contain', 'copy', 'cough', 'cover', 'crown', 
'damage', 'dawn', 'decide', 'defend', 'desire', 'destroy', 
'develop', 'devour', 'dislike', 'divide', 'drop', 'earn', 
'employ', 'encourage', 'enjoy', 'establish', 'evoke', 
'expect', 'explode', 'express', 'fail', 'fetch', 'finish', 
'fit', 'float', 'follow', 'gain', 'gather', 'grant', 
'guard', 'handle', 'happen', 'heat', 'hire', 'hunt', 
'imagine', 'import', 'improve', 'increase', 'intend', 
'invite', 'join', 'jump', 'kick', 'kiss', 'land', 'laugh', 
'like', 'live', 'love', 'maintain', 'measure', 'mention', 
'name', 'notice', 'obey', 'oblige', 'offer', 'order', 'pack',
 'pass', 'place', 'please', 'practise', 'prepare', 'produce',
 'propose', 'punish', 'rain', 'receive', 'refuse', 'remain']

verbs_regular_traduction = ['abandonar', 'absolver', 
'injuriar', 'acelerar', 'aceptar', 'acostumbrar', 
'adquirir', 'sumar', 'admirar', 'adorar', 'avanzar', 
'aconsejar', 'acceder', 'ascender/cantidad', 'anunciar', 
'contestar', 'aparecer', 'acercarse', 'arreglar', 
'preguntar', 'asombrar', 'intentar', 'atraer', 'bañarse', 
'creer', 'culpar', 'llamar', 'cobrar', 'cambiar', 
'reclamar', 'aclarar, limpiar', 'cerrar', 'peinar', 
'mandar', 'comparar', 'componer', 'considerar', 'contener', 
'copiar', 'toser', 'cubrir', 'coronar', 'dañar', 'amanecer',
'decidir', 'defender', 'desear', 'destruir', 'desarrollar', 
'devorar', 'desaprobar', 'dividir', 'dejar caer', 'ganar', 
'emplear', 'animar', 'disfrutar', 'establecer', 'evocar', 
'esperar', 'estallar', 'expresar', 'fallar', 'ir por', 
'acabar', 'ajustar', 'flotar', 'seguir', 'ganar', 'recoger', 
'conceder', 'guardar', 'manejar', 'suceder', 'calentar', 
'alquilar', 'cazar', 'imaginar', 'importar', 'mejorar', 
'aumentar', 'proponerse', 'invitar', 'unir', 'saltar', 
'cocear', 'besar', 'aterrizar', 'reír', 'gustar', 'vivir', 
'amar', 'mantener', 'medir', 'mencionar', 'nombrar', 
'notar, darse cuenta', 'obedecer', 'obligar', 'ofrecer', 
'ordenar', 'empaquetar', 'pasar', 'colocar', 'agradar', 
'practicar', 'preparar', 'producir', 'proponer', 'castigar', 
'llover', 'recibir', 'rehusar', 'permanecer']

verbs_iregular = ['beat', 'become', 'begin', 'bend', 'bet', 
'bite', 'blow', 'break', 'bring', 'broadcast', 'build', 
'burst', 'buy', 'catch', 'choose', 'come', 'cost', 'creep', 
'cut', 'deal', 'dig', 'do', 'draw', 'drink', 'drive', 'eat', 
'fall', 'feed', 'feel', 'fight', 'find', 'flee', 'fly', 
'forbid', 'forget', 'forgive', 'freeze', 'get', 'give', 
'go', 'grow', 'hang', 'have', 'hear', 'hide', 'hit', 'hold', 
'hurt', 'keep', 'kneel', 'know', 'lay', 'lead', 'leave', 
'lend', 'let', 'lie', 'light', 'lose', 'make', 'mean', 
'meet', 'pay', 'put', 'read', 'ride', 'ring', 'rise', 'run', 
'say', 'see', 'seek', 'sell', 'send', 'set', 'sew', 'shake', 
'shine', 'shoot', 'show', 'shrink', 'shut', 'sing', 'sink', 
'sit', 'sleep', 'slide', 'speak', 'spend', 'spit', 'split', 
'spread', 'spring', 'stand', 'steal', 'stick', 'sting', 
'strike', 'swear', 'sweep', 'swim', 'swing', 'take', 
'teach', 'tear', 'tell', 'think', 'throw', 'understand', 
'wake', 'wear', 'weep', 'win', 'write']

verbs_iregular_traduction = ['golpear', 'convertir', 
'comenzar', 'doblar', 'apostar', 'morder', 'soplar', 
'romper', 'traer', 'retransmitir', 'construir', 'reventar', 
'comprar', 'agarrar, coger', 'escoger, elegir', 'venir', 
'costar', 'reptar,arrastrarse', 'cortar', 'repartir', 
'cavar', 'hacer', 'dibujar', 'beber', 'conducir', 'comer', 
'caer', 'alimentar', 'sentir', 'luchar', 'encontrar', 
'escapar', 'volar', 'prohibir', 'olvidar', 'perdonar', 
'helar, congelar', 'conseguir, obtener', 'dar', 'ir', 
'crecer', 'colgar', 'tener', 'oír', 'esconder', 
'golpear, pegar', 'sostener', 'herir, lastimar', 
'guardar, conservar', 'arrodillarse', 'saber, conocer', 
'poner, colocar, acostar (a alguien)', 'guiar', 'dejar', 
'prestar', 'permitir', 'tumbarse', 'iluminar, encender', 
'perder', 'hacer', 'significar', 'encontrar, conocer', 
'pagar', 'poner', 'leer', 'montar', 'sonar', 
'surgir, levantarse', 'correr', 'decir', 'ver', 
'rastrear, buscar a fondo', 'vender', 'enviar', 
'poner, colocar', 'coser', 'agitar', 'brillar', 
'disparar, lanzar', 'mostrar', 'encoger', 'cerrar', 
'cantar', 'hundir', 'sentar', 'dormir', 
'deslizarse, resbalar', 'hablar', 'gastar, pasar (tiempo)', 
'escupir', 'partir, dividir (algo)', 'extender', 
'saltar (de golpe)', 'permanecer parado', 'robar', 
'pegar (algo)', 'picar, escocer', 'golpear, pegar', 
'jurar', 'barrer,deshollinar', 'nadar', 'balancearse', 
'llevar, coger', 'enseñar', 'romper, rasgar', 'decir', 
'pensar, creer', 'lanzar', 'entender', 'despertar', 
'llevar puesto', 'llorar', 'ganar', 'escribir']

verbs_iregular_past = ['beat', 'became', 'began', 'bent', 
'bet', 'bit', 'blew', 'broke', 'brought', 'broadcast', 
'built', 'burst', 'bought', 'caught', 'chose', 'came', 
'cost', 'crept', 'cut', 'dealt', 'dug', 'did', 'drew', 
'drank', 'drove', 'ate', 'fell', 'fed', 'felt', 'fought', 
'found', 'fled', 'flew', 'forbade', 'forgot', 'forgave', 
'froze', 'got', 'gave', 'went', 'grew', 'hung', 'had', 
'heard', 'hid', 'hit', 'held', 'hurt', 'kept', 'knelt', 
'knew', 'laid', 'led', 'left', 'lent', 'let', 'lay', 'lit', 
'lost', 'made', 'meant', 'met', 'paid', 'put', 'read', 
'rode', 'rang', 'rose', 'ran', 'said', 'saw', 'sought', 
'sold', 'sent', 'set', 'sewed', 'shook', 'shone', 'shot', 
'showed', 'shrank', 'shut', 'sang', 'sank', 'sat', 'slept', 
'slid', 'spoke', 'spent', 'spat', 'split', 'spread', 
'sprang', 'stood', 'stole', 'stuck', 'stung', 'struck', 
'swore', 'swept', 'swam', 'swung', 'took', 'taught', 'tore', 
'told', 'thought', 'threw', 'understood', 'woke', 'wore', 
'wept', 'won', 'wrote']

verbs_iregular_participio = ['beaten', 'become', 'begun', 
'bent', 'bet', 'bitten', 'blown', 'broken', 'brought', 
'broadcast', 'built', 'burst', 'bought', 'caught', 'chosen',
'come', 'cost', 'crept', 'cut', 'dealt', 'dug', 'done', 
'drawn', 'drunk', 'driven', 'eaten', 'fallen', 'fed', 
'felt', 'fought', 'found', 'fled', 'flown', 'forbidden', 
'forgotten', 'forgiven', 'frozen', 'gotten', 'given', 
'gone', 'grown', 'hung', 'had', 'heard', 'hidden', 'hit', 
'held', 'hurt', 'kept', 'knelt', 'known', 'laid', 'led', 
'left', 'lent', 'let', 'lain', 'lit', 'lost', 'made', 
'meant', 'met', 'paid', 'put', 'read', 'ridden', 'rung', 
'risen', 'run', 'said', 'seen', 'sought', 'sold', 'sent', 
'set', 'sewn', 'shaken', 'shone', 'shot', 'shown', 
'shrunk', 'shut', 'sung', 'sunk', 'sat', 'slept', 'slid', 
'spoken', 'spent', 'spat', 'split', 'spread', 'sprung', 
'stood', 'stolen', 'stuck', 'stung', 'struck', 'sworn', 
'swept', 'swum', 'swung', 'taken', 'taught', 'torn', 'told',
'thought', 'thrown', 'understood', 'woken', 'worn', 'wept', 
'won', 'written']

def constructor_verb_past(verb):
	if verb in verbs_regular:
		while True:
			if verb[-1] == 'e':
				verb_past = verb + 'd'
				break
			if verb[-1] == 'y':
				verb_past = verb[:-1] + 'ied'
				break
			if not verb[-1] in ['a','e','i','o','u']:
				if verb[-2] in ['a','e','i','o','u']:
					if not verb[-3] in ['a','e','i','o','u']:
						if len(verb) <= 4:
							if not verb[-1] in ['c','x','w','y']:
								verb_past =  verb + verb[-1] + 'ed'
								break
			if verb[-1] == 'c':
				if verb[-2] == ['a','e','i','o','u']:
					verb_past =  verb + 'ked'
					break
			else:
				verb_past = verb + 'ed'
				break
	else:
		verb_past = verbs_iregular_past[verbs_iregular.index(verb)]

	return verb_past

def constructor_participio(verb):
	if verb in verbs_regular:
		while True:
			if verb[-1] == 'e':
				verb_p = verb + 'd'
				break
			if not verb[-1] in ['a','e','i','o','u']:
				if verb[-2] in ['a','e','i','o','u']:
					if not verb[-3] in ['a','e','i','o','u']:
						if len(verb) <= 4:
							if not verb[-1] in ['c','x','w','y']:
								verb_p =  verb + verb[-1] + 'ed '
								break
			if verb[-1] == 'y':
				if verb[-2] in ['a','e','i','o','u']:
					verb_p =  verb + 'ed '
					break
				else: 								
					verb_p = verb[:-1] + 'ied'
					break
			if verb[-1] == 'c':
				if verb[-2] == ['a','e','i','o','u']:
					verb_p =  verb + 'ked'
					break
			else:
				verb_p = verb + 'ed'
				break
	else:
		verb_p = verbs_iregular_participio[verbs_iregular.index(verb)]

	return verb_p

def constructor_verb_continuous(verb):
	while True:
		if verb[-1] == 'e':
			verb_c = verb[:-1] + 'ing'
			break
		if not verb[-1] in ['a','e','i','o','u','y']:
			if verb[-2] in ['a','e','i','o','u']:
				if not verb[-3] in ['a','e','i','o','u']:
					if len(verb) <= 4:
						verb_c =  verb + verb[-1] + 'ing'
						break
		if verb[-1] == 'c':
			if verb[-2] == 'i':
				verb_c =  verb + 'king'
				break
		if verb[-1] == 'l':
			if verb[-2] != 'l':
				verb_c =  verb + 'ling'
				break
			else:
				verb_c =  verb + 'ing'
				break
		if verb[-1] == 'e':
			if verb[-2] == 'i':
				verb_c =  verb[:-2] + 'ying'
				break
		else:
			verb_c = verb + 'ing'
			break

	return verb_c

repeticion_lista_subject = []
repeticion_lista_tense = []

repeticion_lista_tipo = []

for x in tenses_list:
	repeticion_lista_tipo.append([])

repeticion_lista_verb = []
				
def constructor(lista,repeticion_lista,limpia):
	numeros_buscar_lista = [x for x in range(len(lista))]

	while True:
		r = random.choice(numeros_buscar_lista)
		if not r in repeticion_lista:
			if limpia == True:
				repeticion_lista.append(r)
			return lista[r]

		if (len(repeticion_lista) == len(lista)) and (limpia == True):
			del repeticion_lista[:]

def constructor_tense_verb(subject, tense, tipo, verb):
	if tense == 'past':
		if tipo != 'continuous/progressive' or tipo != 'perfect continuous/progressive':
			verb_t_v = constructor_verb_past(verb)
		else:
			verb_t_v = verb
	elif tense == 'present':
		if tipo != 'continuous/progressive' or tipo != 'perfect continuous/progressive':
			if subject in subjects_pronouns_list_3:
				while True:
					if verb[-1] in ['x','z','o']:
						verb_t_v = verb + 'es'
						break
					elif verb[-2:] in ['ss','sh','ch']:
						verb_t_v = verb + 'es'
						break
					elif verb[-1] == 'y':
						if not verb[-2] in ['a','e','i','o','u']:
							verb_t_v = verb[:-1] + 'ies'
							break
						else:
							verb_t_v = verb + 's'
							break
					else:
						verb_t_v = verb + 's'
						break
			else:
				verb_t_v = verb
		else:
			verb_t_v = verb
	elif tense == 'future':
		if tipo != 'continuous/progressive' or tipo != 'perfect continuous/progressive':
			verb_t_v = 'will ' + verb 
		else:
			verb_t_v = verb
	elif tense == 'future -be going to-':
		if tipo != 'continuous/progressive' or tipo != 'perfect continuous/progressive':
			if subject in subjects_pronouns_list_1:
				verb_t_v = verbs_to_be[0] + 'going to ' + verb
			elif subject in subjects_pronouns_list_3:
				verb_t_v = verbs_to_be[2] + 'going to ' + verb
			else:
				verb_t_v = verbs_to_be[1] + 'going to ' + verb 
		else:
			verb_t_v = verb
	elif tense == 'future -be going to- past':
		if tipo != 'continuous/progressive' or tipo != 'perfect continuous/progressive':
			if subject in subjects_pronouns_list_1:
				verb_t_v = verbs_to_be_past[0] + 'going to ' + verb
			elif subject in subjects_pronouns_list_3:
				verb_t_v = verbs_to_be_past[0] + 'going to ' + verb
			else:
				verb_t_v = verbs_to_be_past[1] + 'going to ' + verb 
		else:
			verb_t_v = verb
	elif tense == 'conditional':
		if tipo != 'continuous/progressive' or tipo != 'perfect continuous/progressive':
			verb_t_v = 'would ' + verb
		else:
			verb_t_v = verb
	
	return verb_t_v

def constructor_type(subject, tense, tipo, verb_t_v, verb):
	if tipo == 'simple':
		verb_t = verb_t_v
	elif tipo == 'continuous/progressive':
		if tense == 'past':
			if subject in subjects_pronouns_list_1 or subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be_past[0]
			else:
				verb_t = verbs_to_be_past[1]
		elif tense == 'present':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be[0]
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be[2]
			else:
				verb_t = verbs_to_be[1]
		elif tense == 'future':
			verb_t = 'will ' + 'be '
		elif tense == 'future -be going to-':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be[0] + 'going to ' + 'be '
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be[2] + 'going to ' + 'be '
			else:
				verb_t = verbs_to_be[1] + 'going to ' + 'be '
		elif tense == 'future -be going to- past':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be_past[0] + 'going to ' + 'be '
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be_past[0] + 'going to ' + 'be '
			else:
				verb_t = verbs_to_be_past[1] + 'going to ' + 'be ' 
		elif tense == 'conditional':
			verb_t = 'would ' + 'be '
		verb_t = verb_t + constructor_verb_continuous(verb)

	elif tipo == 'perfect':
		if tense == 'past':
			verb_t = verbs_to_have_past[0]
		elif tense == 'present':
			if subject in subjects_pronouns_list_3:
				verb_t = verbs_to_have[1]
			else:
				verb_t = verbs_to_have[0]
		elif tense == 'future':
			verb_t = 'will ' + 'have '
		elif tense == 'future -be going to-':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be[0] + 'going to ' + 'have '
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be[2] + 'going to ' + 'have '
			else:
				verb_t = verbs_to_be[1] + 'going to ' + 'have '
		elif tense == 'future -be going to- past':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be_past[0] + 'going to ' + 'have '
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be_past[0] + 'going to ' + 'have '
			else:
				verb_t = verbs_to_be_past[1] + 'going to ' + 'have ' 
		else:
			verb_t = 'would ' + 'have '
		verb_t =  verb_t + constructor_participio(verb)

	elif tipo == 'perfect continuous/progressive':
		if tense == 'past':
			verb_t = verbs_to_have_past[0] + 'been '
		elif tense == 'present':
			if subject in subjects_pronouns_list_3:
				verb_t = verbs_to_have[1] + 'been '
			else:
				verb_t = verbs_to_have[0] + 'been '
		elif tense == 'future':
			verb_t = 'will ' + 'have ' + 'been '
		elif tense == 'future -be going to-':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be[0] + 'going to ' + 'have ' + 'been '
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be[2] + 'going to ' + 'have ' + 'been '
			else:
				verb_t = verbs_to_be[1] + 'going to ' + 'have ' + 'been '
		elif tense == 'future -be going to- past':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be_past[0] + 'going to ' + 'have ' + 'been '
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be_past[0] + 'going to ' + 'have ' + 'been '
			else:
				verb_t = verbs_to_be_past[1] + 'going to ' + 'have ' + 'been '
		elif tense == 'conditional':
			verb_t = 'would ' + 'have ' + 'been '

		verb_t = verb_t + constructor_verb_continuous(verb)

	return verb_t

validacion = ''
i=0
c=0
e=0
z=0
print('Conjugador de verbos regulares e irregulares')
print('No duplica consonantes en palabras de mas de una silaba')
print('todo en minusculas [Excepto I] y un solo espacio entre palabras')
input()

while validacion == '':
	os.system('cls')

	subject = constructor(subjects_pronouns_list,repeticion_lista_subject,True)
	tense = constructor(tenses_list,repeticion_lista_tense,True)
	indice = tenses_list.index(tense)
	tipo = constructor(types_list,repeticion_lista_tipo[indice],True)

	print('1. ' + subject)
	print('2. ' + tense)
	print('3. ' + tipo)

	if z <= 4:
		verb = constructor(verbs_regular,repeticion_lista_verb,True)
		print('4. ' + verb)
		print('** (' + verbs_regular_traduction[verbs_regular.index(verb)] + ')')
		z = z+1
	else:
		verb = constructor(verbs_iregular,repeticion_lista_verb,True)
		print('4. ' + verb)
		print('** (' + verbs_iregular_traduction[verbs_iregular.index(verb)] + ')' )
		z = 0
		
	conjugacion = '---' + input('***Ingresa la conjugacion correcta: \n---')

	print('***La conjuación correcta es: ')
	conjugacion_correcta = '---' + subject + constructor_type(subject, tense, tipo, constructor_tense_verb(subject, tense, tipo, verb), verb)
	print(conjugacion_correcta)

	if conjugacion_correcta == conjugacion:
		print('---CORRECTO')
		c = c+1
	else:
		print('---ERROR. INCORRECTO')
		e = e+1
	print(f'intentos: {i+1}')
	validacion = input('Continuar [enter]/ Salir [Cualquier tecla]: ')
	i = i+1

print('intentos')
print(i)
print('correctos')
print(c)
print('incorrectos')
print(e)

input('FIN')