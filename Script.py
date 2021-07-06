import pandas as pd
import numpy as np
from sklearn.preprocessing import *
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/akhil14shukla/IME672A-Course-Project/master/hmeq.csv")

sns.pairplot(df)

df.isna().sum()

