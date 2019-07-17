import math


def askInput():
	while True:
		try:
			num = int(input("Give a number: "))
			return num
		except Exception:
			print("This input is invalid.")

		
		
def main():
	print("Calculator")
	num1 = askInput()
	num2 = askInput()
	while True:
		print("""(1) +
		(2) -
		(3) *
		(4) /
		(5) sin(number1/number2)
		(6) cos(number1/number2)
		(7) Change numbers
		(8) Quit
		""")
		print("Current numbers: ",num1," ",num2)
		selection = input("Please select something(1-6): ")
	
		if selection == "1":
			print("The result is: ",num1+num2)
		elif selection == "2":
			print("The result is: ",num1-num2)
		elif selection == "3":
			print("The result is: ",num1*num2)
		elif selection == "4":
			print("The result is: ",num1/num2)
		elif selection == "5":
			print("The result is: ",math.sin(num1/num2))
		elif selection == "6":
			print("The result is: ",math.cos(num1/num2))
		elif selection == "7":
			num1 = askInput()
			num2 = askInput()
		elif selection == "8":
			print("Thank you!")
			break
			
if __name__ == "__main__":
	main()
	
