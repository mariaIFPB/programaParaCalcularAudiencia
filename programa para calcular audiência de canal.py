#programa para calcular a audiencia de canais

cont7 = 0
cont = 1
cont10 = 0
cont12 = 0
while (cont>0):
	npessoas = eval(input("digite o numero de pessoas na casa:"))
	for i in range(npessoas):
		canalp = int(input("qual o canal preferido?"))
		if (canalp == 7):
			cont7 = cont7 + 1 
		elif (canalp == 10):
			cont10 = cont10 +1 
		elif (canalp == 12):
			cont12 = cont12+1 
		else:
			print("o canal digitado não serve para a pesquisa.")
	parar = str(input("quer continuar?"))
	if (parar == "não"):
		break
		
print("audiencia do canal 7 é : ",cont7)
print("audiencia do canal 10 é:",cont10)
print("audiencia do canal 12 é:",cont12)
