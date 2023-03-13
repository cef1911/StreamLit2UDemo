from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import time

#import plotly as px
#import plotly.figure_factory as ff


"""
# Starting to make demo of streamlit components Kids Fishing Data Science Project

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

# Team A	Role	Fish Caught
# John	Captain	10
# Sara	Data Wrangler	12
# Nick	Team Community Liason	21
# Rex	Statistics Person	7
# Cathy	Asst Captain	14
# st.balloons()

# st.snow()
