# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** that suggests movies similar to the one selected by the user.  
The system uses **machine learning and cosine similarity** and includes a **Streamlit web application (`app.py`)** for interactive recommendations.

---

## 🚀 Project Overview

This project recommends movies based on their **content similarity** such as genres, keywords, cast, and overview.  
Users select a movie, and the system suggests **top 5 similar movies along with posters** fetched using the **TMDB API**.

---

## 🧠 Key Concepts Used

- Content-Based Filtering
- Natural Language Processing (NLP)
- Text Vectorization
- Cosine Similarity
- Machine Learning
- Model Serialization (Pickle)
- API Integration
- Web App Development

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Requests
- TMDB API

---

## 📂 Project Structure

├── app.py
├── movie recommender system.ipynb
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Project Workflow

1. Load movie dataset  
2. Clean and preprocess text data  
3. Convert text into vectors  
4. Compute cosine similarity matrix  
5. Save processed data using pickle  
6. Load model and similarity matrix in `app.py`  
7. Recommend similar movies with posters  

---

## 🎯 Recommendation Logic

- User selects a movie
- Cosine similarity is computed with all other movies
- Top 5 most similar movies are recommended
- Movie posters are fetched using TMDB API

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

yaml
Copy code

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

yaml
Copy code

---

### 3️⃣ Run the Web Application

streamlit run app.py

yaml
Copy code

---

## 🔑 TMDB API Key

This project uses **TMDB API** to fetch movie posters.

- Create an account at: https://www.themoviedb.org/
- Generate an API key
- Replace the API key in `app.py` if required

https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY

yaml
Copy code

---

## 🧪 Example Output

**Selected Movie**
Avatar

markdown
Copy code

**Recommended Movies**
John Carter

Guardians of the Galaxy

Interstellar

Star Trek

Star Wars

yaml
Copy code

---

## 📌 Applications

- Movie streaming platforms
- OTT recommendation engines
- Personalized content discovery
- Entertainment analytics

---

## 📈 Future Enhancements

- Hybrid recommendation system
- User-based collaborative filtering
- Improved UI design
- Deployment on Streamlit Cloud
- Search and filter options

---

## 🧑‍💻 Author

**Shashank Shekhar**  
Machine Learning & Data Science Enthusiast

---

⭐ If you like this project, please **star the repository**!
