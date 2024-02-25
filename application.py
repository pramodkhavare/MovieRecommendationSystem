import pandas as pd
import streamlit as st
import pickle
import requests
import utils
from PIL import Image
import cv2


def set_background(image_url):
    """
    Sets a background image for Streamlit app using CSS.
    """
    page_bg_img = '''
    <style>
    body 
    background-image: url(''' + image_url + ''');
    background-size: cover;
    
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('D:/MachineLearning/Project/MovieRecomendattion/Netflix.jpg')





def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=eb5be20a43287bc0db249815938d32d6")
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id


        # fetch poster from API
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters


movie_dict = pickle.load(open('D:\\MachineLearning\\Project\\MovieRecomendattion\\artifacts\\movie_dict.pkl' ,'rb'))
movies = pd.DataFrame.from_dict(movie_dict())

similarity = pickle.load(open('D:\\MachineLearning\\Project\\MovieRecomendattion\\artifacts\\similarity.pkl' ,'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
"Which movie you want to watch",
(movies["title"].values))

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2 , col3 ,col4, col5, col6 = st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col6:
        st.text(names[5])
        st.image(posters[5])
