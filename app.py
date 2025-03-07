import streamlit as st
import datetime
import requests

'''
# Best ride, fair price 🚕
'''

st.markdown('''
Let's get some informations about your ride!
''')


date = st.date_input(
    'When would you like to be picked up?',
    datetime.date(2025, 3, 7))

time = t = st.time_input(
    'Which time would you like to be picked up?',
    datetime.time(12, 30))

pickup_long = st.number_input('Insert your pickup longitude')

pickup_lat = st.number_input('Insert your pickup latitude')

dropoff_long = st.number_input('Insert your dropoff longitude')

dropoof_lat = st.number_input('Insert your dropoff latitude')

pasenger_count = st.number_input('How many people will be with you?', min_value=1, max_value=8)

'''#Lets get some ride for you!'''

params = {
    'pickup_datetime': datetime.datetime.combine(date, time).strftime('%Y-%m-%d %H:%M:%S'),
    "pickup_longitude": pickup_long,
    'pickup_latitude': pickup_lat,
    "dropoff_longitude": dropoff_long,
    'dropoff_latitude': dropoof_lat,
    "passenger_count": pasenger_count
}

url = 'https://taxifare.lewagon.ai/predict'

if st.button('Research 🔍'):
    # print is visible in the server output, not in the page
    r = requests.get(url, params=params)
    rep = r.json()
    '''The price for the ride:'''
    st.write(rep['fare'], '$')



else:
    st.write('Click me😞')
