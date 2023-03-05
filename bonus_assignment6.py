#TASK 6: Drop Four
#create a list of 6 names

def name_length(names):
    names = ["Michelle", "Ally", "Meli", "Marco", "Anna", "Laura"]
    print (names) #wanted to first print the list of names
    for i in names:
        print(i)
        if len(i) <=4:#We wanted to remove names in list that contain more than 4 characters
            names.remove(i) #we therefore use names.remove to remove those with more than 4 characters
            print(names)    #output is new list with removed names     
# this is so cool! 
        
name_length("")





    






