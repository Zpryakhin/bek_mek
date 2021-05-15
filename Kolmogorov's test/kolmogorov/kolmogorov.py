import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats



df = pd.read_csv('experiment.csv')
df['value'].plot(kind = 'bar')
df1 = pd.DataFrame(data={
    'dfNew': df['value']
})

df1.plot.kde()
#plt.show()

print(stats.kstest(df1['dfNew'], 'norm', (df1['dfNew'].mean(), df1['dfNew'].std()), N=len(df1['dfNew'])))
#statistic = 0,091 (маленькое значение) pvalue=0.755 (большое значение) следовательно распределение очень даже нормальное

