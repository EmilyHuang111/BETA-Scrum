def menu():
  inp = input("1 - Male\n2 - Female\n3 - Exit\n")
  if inp == "1":
    print("male")
  elif inp == "2":
    print("female")
  elif inp == "3":
    print("")
  else: 
    print("Please enter a valid number")
    menu()
menu()
