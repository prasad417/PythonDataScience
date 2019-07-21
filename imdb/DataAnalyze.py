import pandas as pd

nb = pd.read_csv('name.basics.csv', sep='\t', encoding='utf8')
tp = pd.read_csv('title.principals.csv', sep='\t', encoding='utf8')
nd = pd.merge(nb, tp, on='nconst')
nd.to_csv('name.principals.csv', sep='\t', encoding='utf-8', index=False)

np = pd.read_csv('name.principals.csv', sep='\t', encoding='utf8')
tc = pd.read_csv('title.crew.csv', sep='\t', encoding='utf8')
name_principals_crew = pd.merge(tc, np, on='tconst')
name_principals_crew.to_csv('npc.csv', sep='\t', encoding='utf-8', index=False)
print('Test')
