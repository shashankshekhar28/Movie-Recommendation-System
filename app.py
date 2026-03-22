import streamlit as st
import pandas as pd
import pickle
import requests

movies__list=pickle.load(open('movies.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))

def fetch(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f06fa363ff5831bf231f51e780eff330&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies__list[movies__list['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies__list.iloc[i[0]].movie_id
        recommended_movies.append(movies__list.iloc[i[0]].title)
        #fetch movie posters from api
        recommended_movies_posters.append(fetch(movie_id))
    return recommended_movies,recommended_movies_posters

st.title("Movie Recommendation System")

#making selectbox
movieslist=movies__list['title'].values
selected_movie_name = st.selectbox('Select a movie to see similar movies',movieslist)

#making recommend button
if st.button('Recommend'):
    movies,posters=recommend(selected_movie_name)

    # Create 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movies[0])
        st.image(posters[0])

    with col2:
        st.text(movies[1])
        st.image(posters[1])

    with col3:
        st.text(movies[2])
        st.image(posters[2])

    with col4:
        st.text(movies[3])
        st.image(posters[3])

    with col5:
        st.text(movies[4])
        st.image(posters[4])


