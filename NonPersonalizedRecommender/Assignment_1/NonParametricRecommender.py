# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:10:15 2016

@author: akgeni
"""

import pandas as pd
import numpy as np

reviews = pd.DataFrame.from_csv('A1Ratings.csv', sep=',')

mean_of_review = {}

for item in reviews:
    mean_of_review[item] = reviews[item].mean()
    
top5_mean_reviews = sorted(mean_of_review.items(), key = lambda x : x[1], reverse=True)[:5]
print("top5 mean ratings")
for movie, movie_mean in top5_mean_reviews:
    
    print(movie, movie_mean)


print("Calculate percentege rating for movies rated 4+")
# Calculate percentege rating for movies rated 4+ 
four_plus = {}
for item in reviews:
    count = 0
    num_rating = 0
    for val in reviews[item]:
        try:
            rating = int(val)
            num_rating += 1
        except:
            rating = 0
        if rating >= 4:
            count += 1
    four_plus[item] = count / num_rating
          
top5_four_plus_rating = sorted(four_plus.items(), key=lambda x : x[1], reverse=True)[:5]
print("\nTop 5 movies with 4+ ratings")
for movie, four_plus_rating in top5_four_plus_rating:
    print(movie, four_plus_rating)    


# Number of rating for each movie

num_rating_movie = {}
for item in reviews:
    num_rating_movie[item] = reviews[item].count()
top5_most_number_rating = sorted(num_rating_movie.items(), key=lambda x : x[1], reverse=True)[:5]
print("\nTop five movies with highest number of ratings")
for movie, count in top5_most_number_rating:
    print(movie, count)    
    
# Movies that rated with star-wars    
print("\n\n")    
def toInt(val):
    try:
        return int(val)
    except:
        return 0
star_wars = reviews['260: Star Wars: Episode IV - A New Hope (1977)']
star_wars_rating = [ toInt(item) for item in star_wars]
other_movies = [movie for movie in reviews if movie != '260: Star Wars: Episode IV - A New Hope (1977)']
rating_with_starwars = {}
for om in other_movies:
    rating_with_starwars[om] = 0
    for other_r, starwars_r in zip(reviews[om], star_wars_rating):
        
        if starwars_r != 0 and other_r == other_r:
            
            rating_with_starwars[om] += 1
            
print("\nRated with star-wars")
for key, value in rating_with_starwars.items():
    print(key, value)
top5_movies_rated_with_starwars = sorted(rating_with_starwars.items(), key=lambda x : x[1], reverse=True)[:5]        
for movie, rating in top5_movies_rated_with_starwars:
    print(movie, rating)                        


print("\n\n")

        