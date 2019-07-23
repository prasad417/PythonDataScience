import pandas as pd
import  datetime
import numpy as np

# nb = pd.read_csv('./csvfiles/name.basics.csv', sep='\t', encoding='utf8')
# tp = pd.read_csv('./csvfiles/title.principals.csv', sep='\t', encoding='utf8')
# nd = pd.merge(nb, tp, on='nconst', how='outer')
# nd.to_csv('./csvfiles/name.principals.csv', sep='\t', encoding='utf-8', index=False)

# np = pd.read_csv('./csvfiles/name.principals.csv', sep='\t', encoding='utf8')
# tc = pd.read_csv('./csvfiles/title.crew.csv', sep='\t', encoding='utf8')
# name_principals_crew = pd.merge(tc, np, on='tconst', how='outer')
# name_principals_crew.to_csv('./csvfiles/na.pr.crew.csv', sep='\t', encoding='utf-8', index=False)

# npv = pd.read_csv('./csvfiles/na.pr.crew.csv', sep='\t', encoding='utf8')
# tr = pd.read_csv('./csvfiles/title.ratings.csv', sep='\t', encoding='utf8')
# npc_ratings = pd.merge(npv, tr, on='tconst', how='left')
# npc_ratings.to_csv('./csvfiles/npc.ratings.csv', sep='\t', encoding='utf-8', index=False)

# name.basics, title.principals, title.crew, title.ratings

# tb = pd.read_csv('./csvfiles/title.basics.csv', sep='\t', encoding='utf8')
# tb_filter = tb.loc[tb['titleType'] == 'movie']
# ta = pd.read_csv('./csvfiles/title.akas.csv', sep='\t', encoding='utf8')
# title_basics_akas = pd.merge(tb_filter, ta, left_on='tconst', right_on='titleId', how='inner')
# title_basics_akas.to_csv('./csvfiles/title.csv', sep='\t', encoding='utf-8', index=False)

# title.basics, title.akas

# title = pd.read_csv('./csvfiles/title.csv', sep='\t', encoding='utf8')
# npcr = pd.read_csv('./csvfiles/npc.ratings.csv', sep='\t', encoding='utf8')
# movies = pd.merge(title, npcr, on='tconst', how='inner')
# movies.to_csv('./csvfiles/movies.csv', sep='\t', encoding='utf-8', index=False)

print(datetime.datetime.now())
mv = pd.read_csv('./csvfiles/movies.csv', sep='\t', encoding='utf8')
# v = mv[mv.primaryName.isin(['Venkatesh Daggubati'])]
v = mv[np.isin(mv['primaryName'], ['Venkatesh Daggubati'])]
print(datetime.datetime.now())
print(v)
# Select only 2 columns from dataFrame and create a new subset DataFrame
# columnsData = dfObj.loc[ : , ['Age', 'Name'] ]
print('Test')
