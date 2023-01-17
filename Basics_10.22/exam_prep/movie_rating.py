import sys

total_movies = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
worst_movie = None
best_movie = None
combined_rating = 0

for i in range(1, total_movies + 1):
    movie_title = input()
    rating = float(input())

    if rating > highest_rating:
        highest_rating = rating
        best_movie = movie_title
    
    if rating < lowest_rating:
        lowest_rating = rating
        worst_movie = movie_title
    
    combined_rating += rating

print(f"{best_movie} is with highest rating: {highest_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {combined_rating / total_movies:.1f}")
