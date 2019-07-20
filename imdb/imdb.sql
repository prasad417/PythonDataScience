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
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

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
 'Brahmanandam', 'J.D. Chakravarthi') 
AND primaryProfession LIKE 'actor%'
ORDER BY primaryName ASC;

