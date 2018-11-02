import random
import os
import io

subjects_pronouns_list_1 = ['I']
subjects_pronouns_list_2 = ['you']
subjects_pronouns_list_3 = ['he','she', 'it']
subjects_pronouns_list_4 = ['we','they']

subjects_pronouns_list = subjects_pronouns_list_1 + subjects_pronouns_list_2 + subjects_pronouns_list_3 + subjects_pronouns_list_4
subjects_pronouns_list_singular = subjects_pronouns_list_1 + subjects_pronouns_list_2 + subjects_pronouns_list_3
subjects_pronouns_list_plural = subjects_pronouns_list_2 + subjects_pronouns_list_4
###########################################################
tenses_list = ['past', 'present', 'future', 'conditional']
types_list_past = ['simple','continuous/progressive','perfect','perfect continuous/progressive']
types_list_present = types_list_past.copy()
types_list_future = types_list_past.copy()
types_list_future.append('-be going to-')
types_list_conditional = types_list_past.copy()
###########################################################
verbs_to_be = ['am','are','is']
verbs_to_be_past = ['was','were']
verbs_to_be_past = ['was','were']

verbs_to_have = ['have','has']
verbs_to_have_past = ['had']

verbs_to_do = ['do','does']
verbs_to_do_past = ['did']

auxiliar_not = ['not']
auxiliar_would = ['would']
###########################################################
verbs_regular = ['act','add','ask','answer','arrive',
'brush','belong','beg','believe','close','cook','call',
'change']

'''
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

future -be going to-

conditional
conditional continuous
conditional perfect
conditional perfect continuous
'''

repeticion_lista_subject = []
repeticion_lista_tense = []
repeticion_lista_tipo = []
repeticion_lista_verb = []
				
def constructor(lista,repeticion_lista,limpia):
	numeros_buscar_lista = [x for x in range(len(lista))]

	while True:
		r = random.choice(numeros_buscar_lista)

		if (not r in repeticion_lista) and (limpia == True):

			repeticion_lista.append(r)
			numeros_buscar_lista.remove(r)

		if (len(repeticion_lista) == len(lista)) and (limpia == True):
			del repeticion_lista[:]	

		return lista[r]

def constructor_type_list(tense):
	if tense == 'past':
		types_list = types_list_past
	elif tense == 'present':
		types_list = types_list_present
	elif tense == 'future':
		types_list = types_list_future
	elif tense == 'conditional':
		types_list = types_list_conditional
	return types_list

def constructor_verb_regular(subject, tense, tipo, verb):
	if tense == 'past':
		if verb[-1] == 'e':
			verb_s = verb + 'd'
		else:
			verb_s = verb + 'ed'
	elif tense == 'present':
		if subject in subjects_pronouns_list_3:
			if verb[-1] == 'e':
				verb_s = verb + 's'
			else:
				verb_s = verb + 'es'
		else:
			verb_s = verb
	elif tense == 'future':
		verb_s = 'will ' + verb
	elif tense == 'conditional':
		verb_s = 'would ' + verb
	
	return verb_s

def constructor_type(subject, tense, tipo, verb_s, verb):
	if tipo == 'simple':
		verb_t = verb_s
	elif tipo == 'continuous/progressive':
		if tense == 'past':
			if subject in subjects_pronouns_list_1 or subjects_pronouns_list_3:
				verb_t = verbs_to_be_past[0] + ' ' + verb
			else:
				verb_t = verbs_to_be_past[1] + ' ' + verb
		elif tense == 'present':
			if subject in subjects_pronouns_list_1:
				verb_t = verbs_to_be[0] + ' ' + verb
			elif subject in subjects_pronouns_list_3:
				verb_t = verbs_to_be[2] + ' ' + verb
			else:
				verb_t = verbs_to_be[1] + ' ' + verb
		elif tense == 'future':
			verb_t = 'will ' + 'be ' + verb
		elif tense == 'conditional':
			verb_t = 'would ' + 'be ' + verb

		while True:
			if verb_t[-1] == 'e':
				verb_t = verb_t[:-1]
				verb_t =  verb_t + 'ing'
				break
			if not verb_t[-1] in ['a','e','i','o','u']:
				if verb_t[-2] in ['a','e','i','o','u']:
					if not verb_t[-3] in ['a','e','i','o','u']:
						if len(verb_t) <= 4:
							verb_t =  verb_t + verb_t[-1] + 'ing'
							break
			if verb_t[-1] == 'c':
				if verb_t[-2] == 'i':
					verb_t =  verb_t + 'king'
					break
			if verb_t[-1] == 'l':
				verb_t =  verb_t + 'ling'
				break
			if verb_t[-1] == 'e':
				if verb_t[-2] == 'i':
					verb_t =  verb_t[:-2] + 'ying'
					break
			verb_t = verb_t + 'ing'
			break
	elif tipo == 'perfect':
		if tense == 'past':
			verb_t = verbs_to_have_past[0] + ' ' + verb_s
		elif tense == 'present':
			if subject in subjects_pronouns_list_3:
				verb_t = verbs_to_have[1] + ' ' + verb_s
			else:
				verb_t = verbs_to_have[0] + ' ' + verb_s
		elif tense == 'future':
			verb_t = 'will ' + 'have ' + verb
		else:
			verb_t = 'would ' + 'have ' + verb
	elif tipo == 'perfect continuous/progressive':
		if tense == 'past':
			verb_t = verbs_to_have_past[0] + ' been ' + verb
		elif tense == 'present':
			if subject in subjects_pronouns_list_3:
				verb_t = verbs_to_have[1] + ' been ' + verb
			else:
				verb_t = verbs_to_have[0] + ' been ' + verb
		elif tense == 'future':
			verb_t = 'will ' + 'have ' + 'been ' + verb
		elif tense == 'conditional':
			verb_t = 'would ' + 'have ' + 'been ' + verb

		while True:
			if verb_t[-1] == 'e':
				verb_t = verb_t[:-1]
				verb_t =  verb_t + 'ing'
				break
			if not verb_t[-1] in ['a','e','i','o','u']:
				if verb_t[-2] in ['a','e','i','o','u']:
					if not verb_t[-3] in ['a','e','i','o','u']:
						if len(verb_t) <= 4:
							verb_t =  verb_t + verb_t[-1] + 'ing'
							break
			if verb_t[-1] == 'c':
				if verb_t[-2] == 'i':
					verb_t =  verb_t + 'king'
					break
			if verb_t[-1] == 'l':
				verb_t =  verb_t + 'ling'
				break
			if verb_t[-1] == 'e':
				if verb_t[-2] == 'i':
					verb_t =  verb_t[:-2] + 'ying'
					break
			verb_t = verb_t + 'ing'
			break
	elif tipo == '-be going to-':
		if subject in subjects_pronouns_list_1:
			verb_t = verbs_to_be[0] + ' going to ' + verb
		elif subject in subjects_pronouns_list_3:
			verb_t = verbs_to_be[2] + ' going to ' + verb
		else:
			verb_t = verbs_to_be[1] + ' going to ' + verb

	return verb_t
validacion = ''
i=0
c=0
e=0

while validacion == '':
	os.system('cls')

	subject = constructor(subjects_pronouns_list,repeticion_lista_subject,True)
	tense = constructor(tenses_list,repeticion_lista_tense,True)
	tipo = constructor(constructor_type_list(tense),repeticion_lista_tipo,False)
	verb = constructor(verbs_regular,repeticion_lista_verb,True)

	print('1. ' + subject)
	print('2. ' + tense)
	print('3. ' + tipo)
	print('4. ' + verb)
	
	conjugacion = input('***Ingresa la conjugacion correcta: \n')

	print('***La conjuación correcta es: ')

	conjugacion_correcta = subject + ' ' + constructor_type(subject, tense, tipo, constructor_verb_regular(subject, tense, tipo, verb),verb)
	print(conjugacion_correcta)

	if conjugacion_correcta == conjugacion:
		print('CORRECTO')
		c = c+1
	else:
		print('ERROR. INCORRECTO')
		e = e+1
	validacion = input('Continuar [enter]: ')
	i = i+1

print('intentos')
print(i)
print('correctos')
print(c)
print('incorrectos')
print(e)

input('FIN')