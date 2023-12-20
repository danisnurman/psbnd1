import streamlit as st
import pandas as pd
import numpy as np
import math
import random
from mitosheet.streamlit.v1 import spreadsheet

st.write('Hi!')

# df = pd.read_csv(r'https://raw.githubusercontent.com/danisnurman/psbnd1/main/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
# df.head(10)

st.set_page_config(layout="wide")

CSV_URL = 'https://raw.githubusercontent.com/danisnurman/psbnd1/main/diabetes_binary_5050split_health_indicators_BRFSS2015.csv'
new_dfs, code = spreadsheet(CSV_URL)

st.write(new_dfs)
st.code(code)