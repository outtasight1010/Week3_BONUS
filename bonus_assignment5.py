#TASK 5: Reverse a List
fav_movies_list = ["Rocky","The Godfather","Lost in Translation"]

print(fav_movies_list) #output list

#ok, but we must create a function to reverse list of movies
def movies_list2():
    reverse_fav_movies = list("") #assigning reverse_fav_movies list to an (empty list)
    for movie in fav_movies_list:
        reverse_fav_movies =[movie] + reverse_fav_movies
        print(reverse_fav_movies)

movies_list2()










