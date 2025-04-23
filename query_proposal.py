import pandas as pd
import numpy as np
lat_gemini=30.2417

df=pd.read_csv("miles.tsv", sep=';', header=36)
df.columns=['ra_decimal', 'dec_decimal', 'name', 'ra_sex', 'dec_sex','e(b-v)', 'ST']
df=df.drop(['ra_sex', 'dec_sex'], axis=1)
df=df[['name', 'ra_decimal', 'dec_decimal', 'ST', 'e(b-v)']]
df=df.dropna()
df['name']=df['name'].str.strip()
#mask_F=df['ST'].str.contains("F")
#mask_G=df['ST'].str.contains("G")
mask_K=df['ST'].str.contains("K")
mask_M=df['ST'].str.contains("M")
df=df[mask_K+mask_M]
df=df[df['dec_decimal'] < (0)]
df=df.reset_index(drop=True)
ra_dec=df.drop(['ST', 'e(b-v)'], axis=1)
ra_dec=df.sort_values(['ra_decimal'])
print(ra_dec)
for i in np.arange(0,99): print('{} {:.3f} {:.3f}'.format(df['name'][i], df['ra_decimal'][i], df['dec_decimal'][i]))
#for i in np.arange(120,160): print('{} {:.3f} {:.3f}'.format(df['name'][i], df['ra_decimal'][i], df['dec_decimal'][i]))
#for i in np.arange(200,272): print('{} {:.3f} {:.3f}'.format(df['name'][i], df['ra_decimal'][i], df['dec_decimal'][i]))


