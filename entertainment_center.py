from media import Movie
from fresh_tomatoes import open_movies_page

# the goal of my project is to seperate view, data and control
# creating a MVC-alike file structure
# so source files could be individually modified and less prone to mistakes.
# the file structure is as follows:
# Model     : movie_db.csv
#             this file contains only movie data, separated by comma, with each line corresponds to 1 movie
#             it's a table-like data-structure:
#                   1st column: movie title
#                   2nd column: movie trailer URL
#                   3rd column: movie poster URL
#             the 1st line of the data is column title, so the following program needs to ommit it

# View      : fresh_tomatoes.py
#             this file is provided by udacity, with the main goal of producing a webpage with given data

# Control   : entertainment_center.py
#             this file controls the main flow which is the following:
#             1. loop through data file : movie_db.csv
#             2. with each line of the data, create a corresponding Movie object
#             3. append the object into the final movie list
#             4. call function: open_movies_page to show the webpage using the list

movie_list=[]   # final movie list

with open("movie_db.csv","r") as f: # reads the movie data file into f
    is_first_row=True
    for l in f:
        if is_first_row: # this is to ommit the first row of the file which is not movie data but column names
            is_first_row=False
            continue
        
        m=l.split(",") # split each piece of information of 1 movie into a list: m
        
        movie_list.append(Movie(title=m[0],trailer_url=m[1],poster_url=m[2])) # it looks clearer to write out the name of the parameters of the constructor of the Movie class

open_movies_page(movie_list)
