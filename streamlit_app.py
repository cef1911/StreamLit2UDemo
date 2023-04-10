from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import time
# import pyplot as plt

#import plotly as px
#import plotly.figure_factory as ff


"""
# Demo of streamlit components Kids Fishing Data Science Project

DataFrames which will be the team info.
4 teams of 5 Kids
More info to be added consistently
"""



# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

df2 = pd.DataFrame(
    [
        {"Team A": "John", "Role": "Captain", "Fish Caught": 21},
        {"Team A": "Sara", "Role": "Data Wrangler", "Fish Caught": 4},
        {"Team A": "Tony", "Role": "Team Liason", "Fish Caught": 10},
        {"Team A": "Patricia", "Role": "Assistant Captain", "Fish Caught": 6},
        {"Team A": "Tina", "Role": "Statistics Person", "Fish Caught": 30},
    ]
)

# st.dataframe(df, use_container_width=True)
st.dataframe(df2, use_container_width=True)

# chart_data = pd.DataFrame(df
# #     np.random.randn(20, 3),
# #     columns=["a", "b", "c"])

# st.bar_chart(df2)

st.bar_chart(df2, y = 'Team A', x='Fish Caught')

# # Team A Data
# d = {'Team A':['John','Sara','Tony','Patricia','Tina'],
#      'Fish Caught':[21, 4, 10, 6, 30],
#      'Role':['Captain', 'Data Gatherer', 'Statistics Person', 'Team Liason', 'Assistant Captain']}

# teamA = pd.DataFrame(data = d)

# st.bar_chart(teamA, y = 'Team A', x='Fish Caught')

# https://towardsdatascience.com/streamlit-from-scratch-presenting-data-d5b0c77f9622
# # The Incredible Widget Company
# d = {'Quarter':[1,2,3,4],
#      'Widgets':[100,110,112,120],
#      'Wodgets':[50,100,120, 125],
#      'Wudgets':[200,150,100,90]}
     
# salesdf = pd.DataFrame(d)

# Crypto monthly data
dc = {'Fish Caught':[1,2,3,4,5,6,7,8,9,10,11],
     'Fishing Casts':[477,387,444,462,384,297,192,327,221,193,204]}
     #'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

fishdata = pd.DataFrame(data = dc)
st.bar_chart(fishdata, y = 'Fish Caught', x='Fishing Casts')

# import matplotlib.pyplot as plt
# import numpy as np

# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)

# st.pyplot(fig)

# # Pie chart will be used kids team's data, This existing code below is where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 1],
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)

"""
# Demo of Coin Flip
"""
import streamlit as st, random, time    

time.sleep(1)
coins = ['http://re-bol.com/heads.jpg', 'http://re-bol.com/tails.jpg']
coin = random.choice(coins)
st.image(coin)
if st.button('Flip'):
  st.experimental_rerun()

"""
# Demo of Live Webcam Viewer

Credit to:
Nick Antonaccio (nick@com-pute.com)
"""
import streamlit as st

cam=st.selectbox(
  'Choose a Cam', 
  [
    '',
    'pitriverbridge/pitriverbridge.jpg',
    'johnsongrade/johnsongrade.jpg',
    'perez/perez.jpg',
    'mthebron/mthebron.jpg',
    'eurekaway/eurekaway.jpg',
    'sr70us395/sr70us395.jpg',
    'bogard/bogard.jpg',
    'eastriverside/eastriverside.jpg',
  ]
)
if cam:
  st.image('https://cwwp2.dot.ca.gov/data/d2/cctv/image/' + cam)

"""
#Demo of Calculator

Credit to:
Nick Antonaccio (nick@com-pute.com)
"""
import streamlit as st, ast

if 'total' not in st.session_state:
  st.session_state.total=''
if st.button('Clear'): st.session_state.total=''
col1, col2, col3, col4, col5=st.columns([1,1,1,1,4])
if col1.button('1'): st.session_state.total+='1'
if col2.button('2'): st.session_state.total+='2'
if col3.button('3'): st.session_state.total+='3'
if col4.button('+'): st.session_state.total+='+'
if col1.button('4'): st.session_state.total+='4'
if col2.button('5'): st.session_state.total+='5'
if col3.button('6'): st.session_state.total+='6'
if col4.button('-'): st.session_state.total+='-'
if col1.button('7'): st.session_state.total+='7'
if col2.button('8'): st.session_state.total+='8'
if col3.button('9'): st.session_state.total+='9'
if col4.button('.'): st.session_state.total+='.'
if col1.button('0'): st.session_state.total+='0'
if col2.button('*'): st.session_state.total+='*'
if col3.button('/'): st.session_state.total+='/'
if col4.button('='): 
  st.session_state.total=str(eval(st.session_state.total))
st.text_input('Result', st.session_state.total)
