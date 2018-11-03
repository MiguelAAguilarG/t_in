import openpyxl

nombre_direccion_libro_1 = r'C:\Users\Miguel\Documents\PYTHON\t_in'
nombre_libro_1 = 'verbos_irregulares.xlsx'
nombre_hoja_1 = 'Hoja1'

wb = openpyxl.load_workbook(nombre_direccion_libro_1 + '\\' + nombre_libro_1)
hoja = wb[nombre_hoja_1]

a = 0
b = 0
c = False
verbs_iregular = []

for i in range(2,116):
	f = hoja.cell(row=i, column=6).value
	verbs_iregular.append(f.lower())

print(verbs_iregular)