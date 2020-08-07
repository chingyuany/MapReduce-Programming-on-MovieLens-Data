# MapReduce-Programming-on-MovieLens-Data  
MapReduce Programming on MovieLens Data  

Q1 Find the mean, median, and standard deviation of the ratings for each of the movie genres  
To Run:
yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-input /repository/movielens/ratings.csv \
-output intro-to-hadoop/Q1output \
-file Q1mapper.py \
-mapper Q1mapper.py \
-file Q1reducer.py \
-reducer Q1reducer.py \
-file ./movielens/movies.csv


Q2 identify the user who provides the most rating. Which genre does this user watch the most  
To Run:
yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-input /repository/movielens/ratings.csv \
-output intro-to-hadoop/output-movielens-05 \
-file Q2mapper.py \
-mapper Q2mapper.py \
-file Q2reducer.py \
-reducer Q2reducer.py \
-file ./movielens/movies.csv
