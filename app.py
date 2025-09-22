import pickle

import streamlit as st
    
import requests

st.header("Movies Recommendation System")

movies=pickle.load(open('artificats/movie_list.pkl','rb'))

with open('artificats/similartiy_list.pkl', 'rb') as f:
    similaraties = pickle.load(f)

movie_list=movies['title'].values
selected_movie=st.selectbox(
    "TyPe or Select Movie",
    movie_list
)



def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similaraties[index])),reverse=True,key=lambda x:x[1])
    recommended_movies_name=[]
    for i in distances[1:6]:
        recommended_movies_name.append(movies.iloc[i[0]]['title'])
    return recommended_movies_name

if st.button("Show Recommendation"):
    names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(f'1. {names[0]}')
    with col2:
        st.text(f'2. {names[1]}')
    with col3:
        st.text(f'3. {names[2]}')
    with col4:
        st.text(f'4. {names[3]}')
    with col5:
        st.text(f'5. {names[4]}')

    