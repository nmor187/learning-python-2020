import numpy as np
import pandas as pd
import matlibplot.pyplot as plt
sales = pd.read_csv('sales_data.csv',parse_dates=['Date'])
sales.head()
sales.shape()
sales.info()
sales.describe()
