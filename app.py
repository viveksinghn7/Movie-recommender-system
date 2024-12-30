import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=29e9ab27306fa0e750fdb90c4303b6d3&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    similarity_percentages = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        similarity_percentages.append(similarity[index][i[0]] * 100)

    return recommended_movie_names, recommended_movie_posters, similarity_percentages

st.title('Movie Recommender System')
movies = pickle.load(open('models/movie_list.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendations'):
    st.write("")
    recommended_movie_names, recommended_movie_posters, similarity_percentages = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster, similarity in zip(cols, recommended_movie_names, recommended_movie_posters, similarity_percentages):
        with col:
            st.markdown(f"<p style='text-align: center;'>Match: {similarity:.2f}%</p>", unsafe_allow_html=True)
            st.image(poster)
            st.markdown(f"<p style='text-align: center;'>{name}</p>", unsafe_allow_html=True)
