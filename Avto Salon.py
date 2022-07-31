# 20-dars: FUNKSIYADAN QIYMAT QAYTARISH

def avto_info(kompaniya, model, rangi, korobka,yili,narhi=None):
	avto = {'kompaniya':kompaniya,
			'model':model,
			'rang':rangi,
			'korobka':korobka,
			'yil':yili,
			'narh':narhi}
	return avto


print("Saytimizdagi avtolar ro'xatini shakllantiramiz.")
avtolar = []
while True:
	print("\nQuyiadgi ma'lumotlarni kiriting" end='')
	kompaniya = input("Ishlab chiqaruvchi: ")
	model = input("Modeli: ")
	rangi = input("Rangi: ")
	korobka = input("Korobka: ")
	yili = input("Ishlab chiqarilgan yili: ")
	narhi = input("Narhi: ")
	avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
	javob = input("Yana avto qo'shasizmi?(yes/no)": )
	if javob == "no":
		break

print("\nSaloninggizdagi avtolar:")
for avto in avtolar:
	



# def oraliq(min,max):
# 	sonlar = []
# 	while min<max:
# 		sonlar.append(min)
# 		min += 1
# 	return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))