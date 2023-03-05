#TASK 3: Word-Letter Indexing
# We want to compress a string of characters 


def condensed_string():
    my_phrase = "Love Wins!"
    final_result = ("")#first set to empty string
#create letter counter outside of loop
    letter_counter = 1
    for index in range(len(my_phrase)):
        if index ==len(my_phrase)-1: 
            final_result += str(letter_counter) + my_phrase[index]
        elif my_phrase[index]== my_phrase[index +1]:
            letter_counter +=1
        elif my_phrase[index]!= my_phrase[index +1]:
            final_result +=str(letter_counter)+ my_phrase[index]
            letter_counter = 1

    print(final_result)

condensed_string()









