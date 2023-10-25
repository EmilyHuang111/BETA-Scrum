#Welcome message for the body fat percentage calculator. 
print("Welcome! Use the menu to find out your body fat percentage.")

# Functions for stack operation
def create_stack():
    stack = []
    return stack
def push(stack, item):
    stack.append(item)
  
#Function for calculating body fat percentage for males. 
def male():
 try:
   #initializing empty list to store acquired messurements from the user.
   male_body_parts = []

   #Gathering skinfold measurements and other data. 
   for body_part in range(1):
    stack_m = create_stack() 
    che = float(input("Enter chest skinfold (in mm between 10 and 100): "))
    push(stack_m, che) 
    abd = float(input("Enter your abdomen skinfold (in mm between 10 and 100): "))
    push(stack_m, abd)      
    thi = float(input("Enter your thigh skinfold (in mm between 10 and 100): "))
    push(stack_m,thi) 
    wai = float(input("Enter your waist circumference (in m between 0.8 and 1.2): "))
    male_body_parts.append(wai)
    fore = float(input("Enter your forearm circumference (in m between 0.15 and 0.45): "))
    male_body_parts.append(fore)
    age = float(input("Enter your age (in years): "))
    che_abd_thi_sum = 0.0 
    for part in range(3):
      che_abd_thi_sum += stack_m[part]
     # Body density formula needed to calculate body fat %
    body_density = 1.0990750 - 0.0008209*che_abd_thi_sum + 0.0000026*(che_abd_thi_sum)**2 - 0.0002017*(age) - 0.005675*(wai) + 0.018586*(fore)

   #Calculate body fat percentage
    body_fat_percentage = (495/body_density) - 450
   #Check to make sure body fat percentage is larger than 1 and less than 100.
    if body_fat_percentage > 1 and body_fat_percentage < 100:
      print(f"Your body fat percentage is approximately {round(body_fat_percentage,2)}%.")
     
    else: 
     print("Please enter a valid body part configuration.")

 except: print("Please enter a valid number.")
 finally: menu()
  
#Function for calculating body fat percentage for females. 
def female():
  try:
   #Initializing an empty list to store acquired measurements from the user. 
   female_body_parts = []
    #Gathering skinfold measurements and other data.
   for body_part in range(1):
    stack_f = create_stack()  
    tri = float(input("Enter your tricep skinfold (in mm between 10 and 100): "))
    push(stack_f, tri)      
    thi = float(input("Enter your thigh skinfold (in mm between 10 and 100): "))
    push(stack_f, thi) 
    sup = float(input("Enter your suprailiac skinfold (in mm between 10 and 100): "))
    push(stack_f, sup) 
    glu = float(input("Enter your gluteal circumference (in cm between 30 and 150): ")) 
    age = float(input("Enter your age (in years): "))
    female_body_parts.append(age)
     
    tri_thi_sup_sum = 0.0
    for part in range(3):
     tri_thi_sup_sum += stack_f[part]   
     #Body density formula needed to calculate body fat %
    body_density = 1.1470292 - 0.0009376*tri_thi_sup_sum + 0.0000030*(tri_thi_sup_sum)**2 - 0.0001156*age - 0.0005839*glu
     #Calculate body fat percentage 
    body_fat_percentage = (495/body_density) - 450
    if body_fat_percentage > 1 and body_fat_percentage < 100:
     print(f"Your body fat percentage is approximately {round(body_fat_percentage,2)}%.")
    else: print("Please enter a valid body part configuration.")
  except: print("Please enter a valid number.")
  finally: menu()
  
  
def menu():
  #Male or female menu
  inp = input("1 - Male\n2 - Female\n3 - Exit\n")
  if inp == "1":
    male()
  elif inp == "2":
    female()
  #Exits if user enters 3
  elif inp == "3":
    print("")
  else: 
    #Throws exception if user enter something that is not in the menu
    print("Please enter a valid number.")
    menu()
menu()

