#TASK 2: Peanut Butter & Jelly

for num in range(0,101,1):
    print(num) #output prints 0 to 100



def p_b_j(): #created a function for the following program

    for num in range(0,101,1):
        if num %3==0 and num%5==0:# for every number divisible by 3 and 5, output is"peanut butter jelly"
            print("peanut butter jelly")
        elif num %3==0: # for every number divisible by 3, output is "peanut butter"
            print("peanut butter")
        elif num %5==0: #for every number divisible by 5, output is "jelly"
            print("jelly")
        else:
            print(num) #for all other numbers, output is the number
p_b_j()




    

















