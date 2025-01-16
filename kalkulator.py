def add(a,b):
	return a+b

def substract(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	if b!= 0:
		return a/b
	else:
		return "Dzielisz przez zero, błąd"

print("wybierz działanie: 1. Dodawanie | 2. Odejmowanie | 3. Mnożenie | 4. Dzielienie"
wybor = input("Twoj wybor: ")
num1 = float(input("numer 1: ")
num2 = float(input("numer 2: ")

if wybor == "1":
	print("Wynik: ", add(num1,num2))
elif wybor == "2":
	print("Wynik: ", substract(num1,num2))
elif wybor == "3":
	print("Wynik: ",multiply(num1,num2))
elif wybor == "4":
	print("Wynik: ", divide(num1,num2))
else:
	print("Zły input")
