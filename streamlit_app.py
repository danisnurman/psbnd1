import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')

df = pd.read_csv(r'https://raw.githubusercontent.com/danisnurman/psbnd1/main/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
df.head(10)