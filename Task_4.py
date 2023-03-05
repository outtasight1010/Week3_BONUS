#TASK 4: Ingredients

#user chooses an ingredient.
#then we see if choice is actually listed in ingredient [list]
def get_ingredient():

    ingredients = ["flour", "sugar", "milk", "apple sauce"]


    choice = input("Which ingredient would you like? ") 
    while choice not in ingredients:
        print("Sorry, ingredient not available.")
        user_input=input("Would you like to 1.choose again or 2.end? Enter 1 or 2 ")
        if user_input == "1":
            choice = input("Which ingredient would you like to start with? ")
        elif user_input== "2":
            print("End")
        break
    if choice in ingredients:    
        print("Yes, this ingredient is listed.")

get_ingredient()





    

    
    


    


       

    

    


















