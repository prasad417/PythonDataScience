import pandas as pd

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

print('Test')
