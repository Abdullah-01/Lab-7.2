import streamlit as st
import requests


API_URL = "https://fastapi-app-alat.onrender.com/predict"  

st.title("Machine Learning Prediction")
st.write("Enter the features to make a prediction.")

assists = st.number_input("assists", min_value=0.0, max_value=1.0)
minutes_played = st.number_input("minutes played ", min_value=0)
games_injured = st.number_input("games injured ", min_value=0)
award = st.number_input("award ", min_value=0)  
highest_value = st.number_input("highest value ", min_value=0)

if st.button("Predict"):

    payload = {
        "assists": assists,
        "minutes played": minutes_played,
        "games_injured": games_injured,
        "award": award,
        "highest_value": highest_value,

    }
    

    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        prediction = response.json()["pred"]
        st.write(f"The prediction is: {prediction}")
    else:
        st.error("Error making prediction!")