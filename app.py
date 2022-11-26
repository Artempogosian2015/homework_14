from flask import Flask, jsonify
from utils import get_by_title, get_by_years, get_by_cast, get_by_genre, rating_children, rating_family, rating_adult

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/movie/<title›")
def get_film_by_title(title):
    film = get_by_title(title)
    return jsonify(film)


@app.route("/movie/<int:year_13/to/<int:year_2›")
def get_film_years(year_1, year_2):
    films = get_by_years(year_1, year_2)
    return jsonify(films)


@app.route("/rating/children")
def films_for_kids():
    films = rating_children()
    return jsonify(films)


@app.route("/rating/family")
def films_for_family():
    films = rating_family()
    return jsonify(films)


@app.route("/rating/adult")
def films_for_adult():
    films = rating_adult()
    return jsonify(films)


@app.route("/genre/<genre>")
def films_by_genre(genre):
    films = get_by_genre(genre)
    return jsonify(films)


if __name__ == '__main__':
    app.run(debug=True)