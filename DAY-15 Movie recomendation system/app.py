import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Bollywood Movie Recommendation System", layout="centered",initial_sidebar_state="collapsed"
)

@st.cache_resource
def load_models():
    df = pickle.load(open("movies_dataframe.pkl", "rb"))
    knn_model = pickle.load(open("movie_knn_model.pkl", "rb"))
    preprocessor = pickle.load(open("preprocessor.pkl", "rb"))
    return df, knn_model, preprocessor

df, knn_model, preprocessor = load_models()

st.title("Movie Recommendation System")
st.markdown("---")

movie_list = df['Movie_Name'].values
selected_movie = st.selectbox(
    "Search or Select a Movie:", 
    movie_list,
    index=0
)

if st.button("Get Recommendations", type="primary"):
    movie_idx = df[df['Movie_Name'] == selected_movie].index[0]
    
    X_processed = preprocessor.transform(df)
    
    distances, indices = knn_model.kneighbors(X_processed[movie_idx : movie_idx + 1])

    recommended_movies = df.iloc[indices[0]]['Movie_Name'].tolist()[1:]
    recommended_genres = df.iloc[indices[0]]['Genre'].tolist()[1:]
    
    st.subheader("Recommended for you:")

    for i, (movie, genre) in enumerate(zip(recommended_movies, recommended_genres), 1):
        st.success(f"**{i}. {movie}** — *Genre: {genre.title()}*")
        