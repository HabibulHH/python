number = input("Please enter your marks: ")
number =  float(number)
#print(type(number))
if number <= 100 and number >=0:
	if number >= 95:
		print("A+")
	elif number >= 90:
		print("A")
	elif number >= 80:
		print("A-")
	elif number >= 70:
		print("B+")
	elif number >= 60:
		print("B")
	elif number >= 50:
		print("B-")
	elif number >= 40:
		print("C+")
	elif number >= 30:
		print("C")
	elif number < 30:
		print("Fail")
else:
	print("Invalid")