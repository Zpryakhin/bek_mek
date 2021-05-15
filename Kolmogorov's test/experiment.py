import pandas as pd
import matplotlib
import numpy
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'value': [5.06, 5.32, 5.69, 5.63, 5.77, 5.47, 5.72, 5.21, 5.24, 5.03, 4.62, 5.11, 4.86, 4.96, 5.09, 4.95, 5.14, 5.18, 5.03, 4.98, 4.97, 4.92, 5.24, 5.13, 
4.58, 4.72, 4.87, 5.15, 5.03, 5.18, 5.13, 4.86, 5.47, 4.74, 5.23, 5.31, 5.38, 5.07, 5.21, 5.04, 5.19, 5.3, 5.08, 5.43, 5.31, 5.02, 5.22, 5.37, 5.47, 5.49, 5.16]
    })

df.to_csv('experiment.csv')

df = pd.read_csv('experiment.csv')
df['experiment'].plot()

df1 = pd.DataFrame(data={
    'df1': df1['experiments']
})

df1.plot.kde()

