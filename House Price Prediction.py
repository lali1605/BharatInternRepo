#Exploratory data analysis (EDA)
#To learn more about the dataset and the competition, visit the website: House Prices - Advanced Regression Techniques


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np

# modules from sklearn used in regression analysis
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.metrics import mean_squared_error

# module for Q-Q plot
from scipy import stats

# ignore warnings from seaborn and sklearn
import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn

pd.options.display.max_rows = 100
