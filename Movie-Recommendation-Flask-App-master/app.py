import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# =========================
# MovieMind Backend
# =========================

recent_searches = []

ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

ratings = pd.merge(movies, ratings).drop(["genres", "timestamp"], axis=1)

user_ratings = ratings.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)

item_similarity_df = user_ratings.corr(method="pearson")
item_similarity_df.to_csv("item_similarity_df.csv")


def get_similar_movies(movie_name, user_rating):
    similar_score = item_similarity_df[movie_name] * (float(user_rating) - 2.5)
    return similar_score.sort_values(ascending=False)


def getRecommendations(movie, rating):
    try:
        similar_movies = pd.DataFrame()

        similar_movies = pd.concat(
            [similar_movies, get_similar_movies(movie, rating).to_frame().T],
            ignore_index=True
        )

        recommendations = similar_movies.sum().sort_values(ascending=False)

        # Remove searched movie
        recommendations = recommendations.drop(labels=[movie], errors="ignore")

        # Top 8 recommendations
        recommendations = recommendations.head(8)

        return recommendations.index.tolist()

    except Exception:
        return []


@app.route("/")
def home():
    return render_template(
        "index.html",
        recommended_movie=[],
        recent_searches=recent_searches,
        searched_movie=""
    )


@app.route("/recommend", methods=["POST"])
def recommend():
    movie_name = request.form["movie"].strip()
    movie_rating = float(request.form["rating"])

    recommendations = getRecommendations(movie_name, movie_rating)

    if movie_name:
        if movie_name in recent_searches:
            recent_searches.remove(movie_name)

        recent_searches.insert(0, movie_name)

        if len(recent_searches) > 5:
            recent_searches.pop()

    return render_template(
        "index.html",
        recommended_movie=recommendations,
        recent_searches=recent_searches,
        searched_movie=movie_name
    )


@app.route("/clear_history")
def clear_history():
    recent_searches.clear()

    return render_template(
        "index.html",
        recommended_movie=[],
        recent_searches=[],
        searched_movie=""
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
