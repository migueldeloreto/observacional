import pandas as pd


df=pd.read_csv("result.csv")
for i in range(0, len(df)):
	print('{} {:.3f} {:.3f}'.format(df['ID'][i], df['RA2000'][i], df['DE2000'][i]))
	
print("*"*50)
print('{} {:.3f} {:.3f}'.format(df['ID'][23], df['RA2000'][23], df['DE2000'][23]))
print('{} {:.3f} {:.3f}'.format(df['ID'][28], df['RA2000'][28], df['DE2000'][28]))
print('{} {:.3f} {:.3f}'.format(df['ID'][24], df['RA2000'][24], df['DE2000'][24]))
print('{} {:.3f} {:.3f}'.format(df['ID'][19], df['RA2000'][19], df['DE2000'][19]))
print('{} {:.3f} {:.3f}'.format(df['ID'][29], df['RA2000'][29], df['DE2000'][29]))
print('{} {:.3f} {:.3f}'.format(df['ID'][51], df['RA2000'][51], df['DE2000'][51]))
print('{} {:.3f} {:.3f}'.format(df['ID'][25], df['RA2000'][25], df['DE2000'][25]))
print('{} {:.3f} {:.3f}'.format(df['ID'][22], df['RA2000'][22], df['DE2000'][22]))