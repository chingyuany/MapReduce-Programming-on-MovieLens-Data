#!/usr/bin/env python

import sys
import csv
import json

# for nonHDFS run
#movieFile = "./movielens/movies.csv"

# for HDFS run
movieFile = "./movies.csv"

movieList = {}
genreList = {}
userList = {}
with open(movieFile, mode="r") as infile:
    reader = csv.reader(infile)
    for row in reader:
        movieList[row[0]] = {}
        movieList[row[0]]["title"] = row[1]
        movieList[row[0]]["genre"] = row[2]

for oneMovie in sys.stdin:
    oneMovie = oneMovie.strip()
    ratingInfo = oneMovie.split(",")
    
    try:
        userid = ratingInfo[0]
        if userid.find("user") == -1:
            if userid in userList:
                userList[userid] += 1
            else:
                userList[userid] = 1
            genres = movieList[ratingInfo[1]]["genre"]
        
            for genre in genres.split("|"):
                if userid in genreList:
                    if genre in genreList[userid]:
                        genreList[userid][genre] += 1
                    else:
                        genreList[userid][genre] = 1
                else:
                    genreList[userid] = {}
                    genreList[userid][genre] = 1
    except ValueError:
        continue

for userid in userList:
    print ("%s\t%s\t%s" % (userid, userList[userid], json.dumps(genreList[userid])))
