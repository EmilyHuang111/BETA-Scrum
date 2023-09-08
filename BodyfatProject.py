print("Welcome! Use the menu to find out your body fat percentage.")

def male():
  
 try:
   #initializing empty list to store acquired messurements from the user.
   male_body_parts = []
   
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
    che_abd_thi_sum = che + abd + thi
    
     # Body density formula needed to calculate body fat %
    body_density = 1.0990750 - 0.0008209*(che_abd_thi_sum) + 0.0000026*(che_abd_thi_sum)**2 - 0.0002017*(age) - 0.005675*(wai) + 0.018586*(fore)
    male_body_parts.append(body_density)
    body_fat_percentage = (495/body_density) - 450
    if body_fat_percentage > 0:
     print(f"Your body fat percentage is approximately {body_fat_percentage:.2%}%.")
     male_body_parts.pop(-1)
     male_body_parts.append(body_fat_percentage)
    else: print("Please enter a valid body part configuration.")

 except: print("Please enter a valid number.")
 finally: menu()
  

def female():
  try:
   #Similar code for female
   female_body_parts = []
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
    tri_thi_sup_sum = tri + thi + sup
    body_density = 1.1470292 - 0.0009376*tri_thi_sup_sum + (0.0000030*tri_thi_sup_sum)**2 - 0.0001156*age - 0.0005839*glu
    body_fat_percentage = (495/body_density) - 450
    if body_fat_percentage > 0:
     print(f"Your body fat percentage is approximately {body_fat_percentage:.2%}%.")
     female_body_parts.pop(-1)
     female_body_parts.append(body_fat_percentage)
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

