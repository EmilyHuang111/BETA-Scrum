def menu():
  inp = input("1 - Male\n 2 - Female\n 3 - Exit\n")
  if inp == "1":
    print("male")
  elif inp == "2":
    print("female")
  elif inp == "3":
    exit
  else: 
    print("Please enter a valid number")
    menu()
menu()
