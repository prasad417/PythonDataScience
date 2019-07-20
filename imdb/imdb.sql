-- SHOW VARIABLES LIKE "secure_file_priv";

-- SELECT @@GLOBAL.secure_file_priv;
-- DROP DATABASE imdb;

-- CREATE DATABASE imdb;

-- USE imdb;

-- CREATE TABLE `name.basics` (
--   `nconst` text,
--   `primaryName` text,
--   `birthYear` text,
--   `deathYear` text,
--   `primaryProfession` text,
--   `knownForTitles` text
-- );

-- CREATE TABLE `title.akas` (
--   `titleid` text,
--   `ordering` text,
--   `title` text,
--   `region` text,
--   `languages` text,
--   `types` text,
--   `attributes` text,
--   `isOriginalTitle` text
-- );

-- CREATE TABLE `title.basics` (
--   `tconst` text,
--   `titleType` text,
--   `primaryTitle` text,
--   `originalTitle` text,
--   `isAdult` text,
--   `startYear` text,
--   `endYear` text,
--   `runtimeMinutes` text,
--   `genres` text
-- );
-- 	
-- CREATE TABLE `title.crew` (
--   `tconst` text,
--   `directors` text,
--   `writers` text
-- );

-- CREATE TABLE `title.principals` (
--   `tconst` text,
--   `ordering` text,
--   `nconst` text,
--   `category` text,
--   `job` text,
--   `characters` text
-- );

-- CREATE TABLE `title.ratings` (
-- 	`tconst` text,
-- 	`averageRating` text,
-- 	`numVotes` text
-- );

-- LOAD DATA INFILE '/Users/prasaddy/mysql/name.basics.csv' 
-- INTO TABLE `name.basics`
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n';
-- -- IGNORE 1 ROWS;

-- LOAD DATA INFILE '/Users/prasaddy/mysql/title.akas.csv' 
-- INTO TABLE `title.akas`
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n';
-- -- IGNORE 1 ROWS;

-- LOAD DATA INFILE '/Users/prasaddy/mysql/title.basics.csv' 
-- INTO TABLE `title.basics`
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n';
-- -- IGNORE 1 ROWS;

-- LOAD DATA INFILE '/Users/prasaddy/mysql/title.crew.csv' 
-- INTO TABLE `title.crew`
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n';
-- -- IGNORE 1 ROWS;

-- LOAD DATA INFILE '/Users/prasaddy/mysql/title.ratings.csv' 
-- INTO TABLE `title.ratings`
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n';
-- -- IGNORE 1 ROWS;

-- LOAD DATA INFILE '/Users/prasaddy/mysql/title.principals.csv' 
-- INTO TABLE `title.principals`
-- FIELDS TERMINATED BY '\t' 
-- LINES TERMINATED BY '\n';
-- -- IGNORE 1 ROWS;

-- SELECT COUNT(nconst) FROM `name.basics`;
-- SELECT COUNT(titleid) FROM `title.akas`;
-- SELECT COUNT(tconst) FROM `title.basics`;
-- SELECT COUNT(tconst) FROM `title.crew`;
-- SELECT COUNT(tconst) FROM `title.principals`;

SELECT * FROM imdb.`name.basics` 
WHERE primaryName IN ('Taraka Rama Rao Nandamuri', 'Akkineni Nageshwara Rao', 'S.V. Ranga Rao', 'Krishna Ghattamanen', 'Venkatesh Daggubati', 'Chiranjeevi', 'Mahesh Babu', 'Pawan Kalyan', 'N.T. Rama Rao Jr.', 'Nandamuri Balakrishna', 'Allu Arjun', 'Nagarjuna Akkineni',
 'Prabhas', 'Ravi Teja', 'Nani', ' Nikhil Siddharth', 'Rana Daggubati', 'Ram Charan', 'Jagapathi Babu', 'Nithiin', 'Naga Chaitanya Akkineni', 'Sharvanand', 'Allari Naresh',
 'Tottempudi Gopichand', 'Ram Pothineni', 'Ram Pothineni', 'Varun Tej', 'Sai Dharam Tej', ' Sumanth', 'Akhil Akkineni', 'Vishnu Manchu', 'Manoj Kumar Manchu',
 'Sai Srinivas Bellamkonda', 'Nara Rohith', 'Mohan Babu', 'Naga Shaurya', 'Sundeep Kishan', 'Varun Sandesh', 'Kalyan Ram', 'Aadi', 'Rajendra Prasad', 'Allu Sirish',
 ' Vijay Deverakonda', ' Adivi Sesh', 'Satyanarayana Kaikala', 'Sobhan Babu', 'Krishnamraju', 'Uday Kiran', 'Venu Thottempudi', 'Vennela Kishore', 'Gummadi', 'Ali',
 'Brahmanandam', 'J.D. Chakravarthi', ' J.V. Somayajulu', 'Sumanth', 'Navdeep', 'Prakash Raj') 
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;

SELECT * FROM imdb.`name.basics` 
WHERE primaryName IN ('Rajinikanth', 'Kamal Haasan', 'Ajith Kumar', 'Joseph Vijay', 'Suriya', 'Vikram', 'Dhanush', 'Karthi', 'Vishal', 'Jiiva', 'Arya', 'Siddharth', 'Madhavan', 
'Srikanth', 'Jayam Ravi', 'T.R. Silambarasan', 'Arvind Swamy', 'Arjun Sarja', 'Prabhu', 'Prabhu Deva', 'Vijayakanth', 'Sathyaraj', 'Sarath Kumar', 'Raj Kiran') 
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;

SELECT * FROM imdb.`name.basics` 
WHERE primaryName IN ('Mohanlal', 'Mammootty', 'Dileep', 'Prithviraj Sukumaran', 'Dulquer Salmaan', 'Suresh Gopi', 'Jayaram') 
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;

SELECT * FROM imdb.`name.basics` 
WHERE primaryName IN ('Puneeth Rajkumar', 'Sudeep', 'Shivarajkumar', 'Upendra', 'Ambarish', 'Yash') 
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;

SELECT * FROM imdb.`name.basics` 
WHERE primaryName IN ('Johnny Depp', 'Al Pacino', 'Robert De Niro', 'Kevin Spacey', 'Denzel Washington', 'Russell Crowe', 'Brad Pitt', 'Leonardo DiCaprio', 'Tom Cruise', 
'John Travolta', 'Arnold Schwarzenegger', 'Sylvester Stallone', 'Christian Bale', 'Morgan Freeman', 'Keanu Reeves', 'Nicolas Cage', 'Hugh Jackman', 'Edward Norton',
'Bruce Willis', 'Tom Hanks', 'Will Smith', 'Sean Connery', 'Vin Diesel', 'Matt Damon', 'Richard Gere', 'Clive Owen', 'Mel Gibson', 'George Clooney','Jack Nicholson',
'Tom Hardy', 'Robert Downey Jr.', 'Orlando Bloom', 'Ian McKellen', 'Antonio Banderas', 'Guy Pearce', 'Samuel L. Jackson','Gerard Butler', 'Simon Baker', 'Clint Eastwood') 
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;

SELECT * FROM imdb.`name.basics` 
WHERE primaryName IN (
'Dilip Kumar', 'Raj Kapoor', 'Dev Anand', 'Amitabh Bachchan', 'Salman Khan', 'Rajesh Khanna', 'Shah Rukh Khan', 'Aamir Khan', 'Dharmendra', 'Akshay Kumar', 'Ashok Kumar',
'Sunil Dutt', 'Sanjeev Kumar', 'Naseeruddin Shah', 'Anil Kapoor', 'Jeetendra', 'Sanjay Dutt', 'Rajendra Kumar', 'Vinod Khanna', 'Nana Patekar', 'Shammi Kapoor', 'Guru Dutt', 
'Sunny Deol', 'Mithun Chakraborty', 'Om Puri', 'Manoj Kumar', 'Pran', 'Prithviraj Kapoor', 'Rishi Kapoor', 'Shatrughan Sinha', 'Saif Ali Khan', 'Hrithik Roshan', 'Feroz Khan',
'Randhir Kapoor', 'Govinda', 'Jackie Shroff', 'Raaj Kumar', 'Sunil Shetty', 'Balraj Sahni', 'Kishore Kumar', 'Emraan Hashmi', 'Amjad Khan', 'Irrfan Khan', 'Nawazuddin Siddiqui',
'Ranbir Kapoor', 'Amol Palekar', 'Amrish Puri', 'Anupam Kher', 'Vinod Mehra', 'Sanjay Khan', 'Shahid Kapoor', 'Kay Kay Menon', 'Alok Nath', 'Kader Khan', 'Manoj Bajpayee',
'Om Prakash', 'Prem Chopra', 'Shakti Kapoor', 'John Abraham', 'Raj Babbar', 'Rakesh Roshan', 'Sanjay Kapoor', 'Bobby Deol', 'Ranveer Singh', 'Varun Dhawan', 'Ranjeet',
'Johnny Lever', 'Imran Khan', 'Riteish Deshmukh', 'Sidharth Malhotra', 'Arjun Kapoor', 'Abhishek Bachchan', 'Gulshan Grover', 'Fardeen Khan', 'Randeep Hooda', 'Paresh Rawal',
'Arjun Rampal', 'Akshaye Khanna', 'Pulkit Samrat', 'Sushant Singh Rajput', 'Raza Murad', 'Pankaj Kapur', 'Sanjay Mishra', 'Farooq Shaikh', 'Farhan Akhtar', 'Abhay Deol',
'Tiger Shroff', 'Arbaaz Khan', 'Vivek Oberoi', 'Aditya Pancholi', 'Deepak Tijori', 'Mohnish Bahl', 'Zayed Khan', 'Annu Kapoor', 'Ayushmann Khurrana', 'Fawad Khan',
'Arshad Warsi')
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;
