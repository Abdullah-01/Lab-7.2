import streamlit as st
import requests
from PIL import Image

API_URL = "https://lab-7-2.onrender.com/predict"  

st.title("Player's Current price Prediction")
st.image('img.gif')
st.write("Enter the features to make a prediction for players current price.")

assists = st.number_input("assists", min_value=0.0, max_value=1.0)
minutes_played = st.number_input("minutes played ", min_value=0)
games_injured = st.number_input("games injured ", min_value=0)
award = st.number_input("award ", min_value=0)  
highest_value = st.number_input("highest value ", min_value=0)

if st.button("Predict"):

    payload = {
        "assists": assists,
        "minutes_played": minutes_played,
        "games_injured": games_injured,
        "award": award,
        "highest_value": highest_value,
    }
    

    response = requests.post(API_URL, json=payload)
    x=""
    if response.status_code == 200:
        prediction = response.json()["pred"]
        if prediction == 0:
            x = "Cheap price"
        elif  prediction == 1:
            x = "Good price"  
        else:
            x="High price"    
        st.write(f"The prediction is: {x}")
    else:
        st.error("Error making prediction!")