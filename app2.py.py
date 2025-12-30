import streamlit as st
import requests
st.title("Weather Report")
API_KEY = "df85785afc6002c4afc29f38eaa7cebc"
city = st.text_input("Enter City Name")
if st.button("Get Weather"):
    if city:
        url = ("https://api.openweathermap.org/data/2.5/weather"f"?q={city}&appid={API_KEY}&units=metric")
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            st.error("city not found")
        else:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            st.success(f"weather report - {city.title()}")
            st.write(f"Temperature: {temp} c")
            st.write(f"Humidity   : {humidity}%")
            st.write(f"condition  : {condition}")
    else:
        st.warning("please enter a city name")