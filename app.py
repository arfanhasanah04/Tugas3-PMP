from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for movies
movies = [
    {"id": 1, "title": "Inception", "description": "A mind-bending thriller by Christopher Nolan.", "poster": "https://via.placeholder.com/300x450?text=Inception", "genre": "Sci-Fi", "duration": "148 minutes", "release_year": "2010", "rating": "8.8"},
    {"id": 2, "title": "The Matrix", "description": "A sci-fi classic about the nature of reality.", "poster": "https://via.placeholder.com/300x450?text=The+Matrix", "genre": "Action, Sci-Fi", "duration": "136 minutes", "release_year": "1999", "rating": "8.7"},
    {"id": 3, "title": "Interstellar", "description": "A journey through space and time to save humanity.", "poster": "https://via.placeholder.com/300x450?text=Interstellar", "genre": "Sci-Fi, Drama", "duration": "169 minutes", "release_year": "2014", "rating": "8.6"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movies')
def movie_list():
    return render_template('movies.html', movies=movies)

@app.route('/movies/<int:movie_id>')
def movie_detail(movie_id):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if not movie:
        return "Movie not found", 404
    return render_template('movie_detail.html', movie=movie)

@app.route('/movies/info/<int:movie_id>')
def movie_info(movie_id):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if not movie:
        return "Movie not found", 404
    return render_template('movie_info.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
