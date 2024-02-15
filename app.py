import streamlit as st
import pickle
import pandas as pd
import numpy as np
#import xgboost
#from xgboost import XGBRegressor

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title("Cricket Score Predictor")

col = st.columns(2)
col1 = col[0]
with col1:
    batting_teams= st.selectbox("Select batting teams",sorted(teams))
col2 = col[1]
with col2:
    bowling_team = st.selectbox("Select bowling team",sorted(teams))
    
city = st.selectbox('Select city',sorted(cities))

coll = st.columns(3)    
col3 = coll[0]
with col3:
    current_score = st.number_input('Current Score')
col4 = coll[1]
with col4:
    overs = st.number_input("overs done(works for >5)")
col5 = coll[2]
with col5:
    wickets = st.number_input('Wicket out')
        
last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120-(overs*6)
    wickets_left = 10-wickets
    crr = current_score/overs
    
    input_df = pd.DataFrame({'batting_team':[batting_teams],
         'bowling_team':[bowling_team],
         'city':[city],
         'current_score':[current_score],
         'balls_left':[balls_left],
         'wickets_left':[wickets_left],
         'crr':[crr],
         'last_five':[last_five]})

    #st.table(input_df)
    #st.text(xgboost.__version--)
    result = pipe.predict(input_df)
    st.header('Predicted Score - '+str(int(result[0])))
