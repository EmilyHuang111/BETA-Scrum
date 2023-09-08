#Welcome message for the body fat percentage calculator. 
print("Welcome! Use the menu to find out your body fat percentage.")

#Function for calculating body fat percentage for males. 
def male():
 try:
   #initializing empty list to store acquired messurements from the user.
   male_body_parts = []

   #Gathering skinfold measurements and other data. 
   
   for body_part in range(1):
    che = float(input("Enter chest skinfold (in mm): "))
    male_body_parts.append(che)
    abd = float(input("Enter your abdomen skinfold (in mm): "))
    male_body_parts.append(abd)
    thi = float(input("Enter your thigh skinfold (in mm): "))
    male_body_parts.append(thi)
    wai = float(input("Enter your waist circumference (in m): "))
    male_body_parts.append(wai)
    fore = float(input("Enter your forearm circumference (in m): "))
    male_body_parts.append(fore)
    age = float(input("Enter your age (in years): "))
    male_body_parts.append(age)
    che_abd_thi_sum = male_body_parts[0] + male_body_parts[1] + male_body_parts[2]
    
     # Body density formula needed to calculate body fat %
    body_density = 1.0990750 - 0.0008209*che_abd_thi_sum + (0.0000026*(che_abd_thi_sum)**2) - 0.0002017*(age) - 0.005675*(wai) + 0.018586*(fore)

   #Calculate body fat percentage
    # print(body_density)
    body_fat_percentage = (495/body_density) - 450
    # print(body_fat_percentage)
    if body_fat_percentage >= 0 and body_fat_percentage < 100:
      print(f"Your body fat percentage is approximately {round(body_fat_percentage,2)}%")
     #Remove body density and update with body fat percentage in the list.
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
    tri = float(input("Enter your tricep skinfold (in mm): "))
    female_body_parts.append(tri)
    thi = float(input("Enter your thigh skinfold (in mm): "))
    female_body_parts.append(thi)
    sup = float(input("Enter your suprailiac skinfold (in mm): "))
    female_body_parts.append(sup)
    glu = float(input("Enter your gluteal circumference (in m): "))
    female_body_parts.append(glu)
    age = float(input("Enter your age (in years): "))
    female_body_parts.append(age)
    tri_thi_sup_sum = female_body_parts[0] + female_body_parts[1] + female_body_parts[2]
     #Body density formula needed to calculate body fat %
    body_density = 1.1470292 - 0.0009376*tri_thi_sup_sum + (0.0000030*tri_thi_sup_sum)**2 - 0.0001156*age - 0.0005839*glu
     #Calculate body fat percentage 
    body_fat_percentage = (495/body_density) - 450
    print("********************************") 
    print(body_fat_percentage)
    if body_fat_percentage >= 0 and body_fat_percentage < 100:
     print(f"Your body fat percentage is approximately {body_fat_percentage:.2%}.")
      #Remove body density and update with body fat percentage in the list.
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

