import pandas as pd
import csv 
import plotly.figure_factory as pff
df = pd.read_csv('data.csv')
fig = pff.create_distplot([df['Height(Inches)'].tolist()],['height'],show_hist = False)
fig.show()