import pandas as pd
import datetime
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
actor_list = [
'Aadi Pudipeddi', 'Adivi Sesh', 'Akhil Akkineni', 'Akkineni Nageshwara Rao', 'Ali Basha Mohammad', 'Allari Naresh', 'Allu Arjun', 'Allu Sirish',
    'Brahmanandam', 'Chiranjeevi Konidela', 'Gopichand Tottempudi', 'Gummadi Venkateswara Rao', 'J.D. Chakravarthi', 'J.V. Somayajulu', 'Jagapathi Babu', 'Kalyan Ram',
    'Krishna Ghattamaneni', 'Krishnamraju', 'Mahesh Babu Ghattamaneni', 'Manoj Kumar Manchu', 'Mohan Babu Manchu', 'N.T. Rama Rao Jr.', 'Naga Chaitanya Akkineni', 'Naga Shaurya',
    'Nagarjuna Akkineni', 'Nandamuri Balakrishna', 'Nani Ghanta', 'Nara Rohith', 'Navdeep Pallapolu', 'Nikhil Siddharth', 'Nithiin Kumar Reddy',
    'Pawan Kalyan Konidela', 'Prabhas Raju Uppalapati', 'Prakash Raj', 'Rajendra Prasad Gadde', 'Ram Charan Konidela', 'Ram Pothineni',  'Rana Daggubati', 'Ravi Teja Bhupatiraju', 'S.V. Ranga Rao',
    'Sai Dharam Tej', 'Sai Srinivas Bellamkonda', 'Satyanarayana Kaikala', 'Sharvanand Myneni', 'Sobhan Babu Uppu', 'Srikanth Meka', 'Sumanth Yarlagadda', 'Sundeep Kishan',
    'Taraka Rama Rao Nandamuri', 'Uday Kiran', 'Varun Sandesh', 'Varun Tej',  'Venkatesh Daggubati', 'Vennela Kishore Bokkala', 'Venu Thottempudi', 'Vijay Deverakonda',
'Vishnu Manchu',
'Rajinikanth Gaekwad', 'Kamal Haasan', 'Ajith Kumar P', 'Joseph Vijay', 'Suriya Sivakumar', 'Vikram Chiyaan', 'Dhanush', 'Karthi Sivakumar',
    'Vishal Krishna Reddy', 'Jiiva Amar Choudary', 'Arya Jamshad Cethirakath', 'Siddharth Suryanarayan', 'Madhavan Ranganathan','Jayam Ravi', 'T.R. Silambarasan',
    'Arvind Swamy', 'Arjun Sarja', 'Prabhu Ganesan', 'Prabhu Deva Sundar', 'Vijayakanth', 'Sathyaraj', 'Sarath Kumar Ramanathan', 'Rajkiran Mohideen Abdul Khadar',
'Lawrence Raghavendra',
    'Mohanlal', 'Mammootty', 'Dileep', 'Prithviraj Sukumaran', 'Dulquer Salmaan', 'Suresh Gopi', 'Jayaram',
    'Puneeth Rajkumar', 'Sudeep', 'Shivarajkumar', 'Upendra', 'Ambarish', 'Yash',
'Dilip Kumar', 'Raj Kapoor', 'Dev Anand', 'Amitabh Bachchan', 'Salman Khan', 'Rajesh Khanna', 'Shah Rukh Khan',
    'Aamir Khan', 'Dharmendra', 'Akshay Kumar', 'Ashok Kumar',
    'Sunil Dutt', 'Sanjeev Kumar', 'Naseeruddin Shah', 'Anil Kapoor', 'Jeetendra', 'Sanjay Dutt', 'Rajendra Kumar',
    'Vinod Khanna', 'Nana Patekar', 'Shammi Kapoor', 'Guru Dutt',
    'Sunny Deol', 'Mithun Chakraborty', 'Om Puri', 'Manoj Kumar', 'Pran', 'Prithviraj Kapoor', 'Rishi Kapoor',
    'Shatrughan Sinha', 'Saif Ali Khan', 'Hrithik Roshan', 'Feroz Khan',
    'Randhir Kapoor', 'Govinda', 'Jackie Shroff', 'Raaj Kumar', 'Sunil Shetty', 'Balraj Sahni', 'Kishore Kumar',
    'Emraan Hashmi', 'Amjad Khan', 'Irrfan Khan', 'Nawazuddin Siddiqui',
    'Ranbir Kapoor', 'Amol Palekar', 'Amrish Puri', 'Anupam Kher', 'Vinod Mehra', 'Sanjay Khan', 'Shahid Kapoor',
    'Kay Kay Menon', 'Alok Nath', 'Kader Khan', 'Manoj Bajpayee',
    'Om Prakash', 'Prem Chopra', 'Shakti Kapoor', 'John Abraham', 'Raj Babbar', 'Rakesh Roshan', 'Sanjay Kapoor',
    'Bobby Deol', 'Ranveer Singh', 'Varun Dhawan', 'Ranjeet',
    'Johnny Lever', 'Imran Khan', 'Riteish Deshmukh', 'Sidharth Malhotra', 'Arjun Kapoor', 'Abhishek Bachchan',
    'Gulshan Grover', 'Fardeen Khan', 'Randeep Hooda', 'Paresh Rawal',
    'Arjun Rampal', 'Akshaye Khanna', 'Pulkit Samrat', 'Sushant Singh Rajput', 'Raza Murad', 'Pankaj Kapur',
    'Sanjay Mishra', 'Farooq Shaikh', 'Farhan Akhtar', 'Abhay Deol',
    'Tiger Shroff', 'Arbaaz Khan', 'Vivek Oberoi', 'Aditya Pancholi', 'Deepak Tijori', 'Mohnish Bahl', 'Zayed Khan',
    'Annu Kapoor', 'Ayushmann Khurrana', 'Fawad Khan',
'Arshad Warsi',
    'Johnny Depp', 'Al Pacino', 'Robert De Niro', 'Kevin Spacey', 'Denzel Washington', 'Russell Crowe', 'Brad Pitt', 'Leonardo DiCaprio', 'Tom Cruise',
'John Travolta', 'Arnold Schwarzenegger', 'Sylvester Stallone', 'Christian Bale', 'Morgan Freeman', 'Keanu Reeves', 'Nicolas Cage', 'Hugh Jackman', 'Edward Norton',
'Bruce Willis', 'Tom Hanks', 'Will Smith', 'Sean Connery', 'Vin Diesel', 'Matt Damon', 'Richard Gere', 'Clive Owen', 'Mel Gibson', 'George Clooney','Jack Nicholson',
'Tom Hardy', 'Robert Downey Jr.', 'Orlando Bloom', 'Ian McKellen', 'Antonio Banderas', 'Guy Pearce', 'Samuel L. Jackson','Gerard Butler', 'Simon Baker', 'Clint Eastwood'
]
mv = pd.read_csv('./csvfiles/movies.csv', sep='\t', encoding='utf8')
# v = mv[mv.primaryName.isin(['Venkatesh Daggubati'])]
v = mv[np.isin(mv['primaryName'], actor_list)]
print(datetime.datetime.now())
print(v)
# Select only 2 columns from dataFrame and create a new subset DataFrame
# columnsData = dfObj.loc[ : , ['Age', 'Name'] ]

#nb = pd.read_csv('./csvfiles/name.basics.csv', sep='\t', encoding='utf8')
#nb_cl = nb[['nconst', 'primaryName', 'primaryProfession']]
#nb_cl.to_json(r'./csvfiles/nb.json', orient='records')
print('Test')
