# 🎬 MovieMind

**MovieMind** is an AI-powered movie recommendation platform that helps users discover movies based on their preferences. The application uses collaborative filtering with **Pearson Correlation** to recommend movies that have similar user-rating patterns.

The project provides a clean, modern web interface built with Flask and demonstrates how recommendation systems can be integrated into a full-stack web application.

---

## ✨ Features

* 🎥 Personalized movie recommendations
* ⭐ User rating input for better recommendations
* 🧠 Collaborative Filtering using Pearson Correlation
* 📊 Similarity Matrix generation
* 🕘 Recent Search History (Last 5 Searches)
* 🗑️ Clear Search History
* 📖 About MovieMind page explaining the recommendation process
* 🌙 Modern Netflix-inspired Dark UI
* 📱 Responsive web interface

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Pandas
* NumPy

### Machine Learning

* Collaborative Filtering
* Pearson Correlation Similarity

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Dataset

* MovieLens Dataset

---

## 📂 Project Structure

```
MovieMind
│
├── static/
│   ├── style.css
│   ├── movies.jpg
│   └── ...
│
├── templates/
│   ├── index.html
│   └── about.html
│
├── app.py
├── movies.csv
├── ratings.csv
├── item_similarity_df.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. The user enters a movie title.
2. The user provides a rating (1–5).
3. MovieMind searches the similarity matrix.
4. Pearson Correlation identifies similar movies.
5. The searched movie is removed from the results.
6. The Top 8 most relevant movies are displayed.

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/MovieMind.git
cd MovieMind
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🖼️ Screenshots

screenshots:

* Home Page
* Recommendation Results
* Recent Searches
* About MovieMind

---

## 📌 Future Improvements

* User Authentication
* Watchlist & Favorites
* Movie Posters using TMDB API
* Search Autocomplete
* Recommendation History Database
* Hybrid Recommendation System
* Cloud Deployment
* Docker Support

---

## 📖 Learning Outcomes

Through this project I explored:

* Recommendation Systems
* Collaborative Filtering
* Pearson Correlation
* Flask Web Development
* Data Processing using Pandas
* Frontend Integration with Flask
* UI/UX Improvements
* Software Project Structuring

---

## 🤝 Contributing

Contributions, feature suggestions, and improvements are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

## 📄 License

This project is intended for educational and learning purposes.
