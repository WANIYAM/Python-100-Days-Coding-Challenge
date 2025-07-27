# 91.Day 91: Movie Recommendation App (Basic Static Version)
# Input favorite movie.
# Show 3-5 static recommendations (for now).

# Static movie recommendation dictionary
recommendations = {
    "Inception": ["Interstellar", "The Prestige", "Tenet", "Shutter Island", "Memento"],
    "Titanic": ["The Notebook", "A Walk to Remember", "The Great Gatsby", "Romeo + Juliet", "P.S. I Love You"],
    "Avengers": ["Iron Man", "Captain America: Civil War", "Thor: Ragnarok", "Guardians of the Galaxy", "Spider-Man: No Way Home"],
    "The Dark Knight": ["Batman Begins", "The Dark Knight Rises", "Joker", "V for Vendetta", "Logan"],
    "Forrest Gump": ["The Green Mile", "Cast Away", "The Shawshank Redemption", "Rain Man", "A Beautiful Mind"]
}

# Get user input
fav_movie = input("Enter your favorite movie: ").strip()

# Get recommendations
suggestions = recommendations.get(fav_movie, ["Sorry, no recommendations found. Try another popular movie."])

# Display result
print("\nRecommended movies:")
for movie in suggestions:
    print(f"- {movie}")
