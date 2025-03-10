while True:
	try:
		user = input("Insert number (or type 'exit' to stop): ")
		if user == "exit":
			print("Exiting program. Goodbye!")
			break
			
		check_number = int(user)
		check_number = abs(check_number)
		
		if check_number % 2 == 0:
			print(f"Number {check_number} is an even number.")
		else:
			print(f"Number {check_number} is an odd number.")
	except:
		print("Invalid input. Please enter a valid number or type 'exit' to stop.")