import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')

train = pd.read_csv('diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
train.head(10)