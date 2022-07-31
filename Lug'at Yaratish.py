lugat = ""
while True:
	Inglizcha = (input("Qiymat kiriting, agar to'xtatmoqchi bo'lsangiz stop deb yozing:  "))
	if Inglizcha == "stop":
		print("Lug'at tayyor bo'ldi: \n ")
		print(lugat)
		break
	Uzbekcha = (input(f"{(Inglizcha)} so'zning Uzbekchasini kiriting: "))
	lugat = lugat + (f"{Inglizcha}-{Uzbekcha} \n") 