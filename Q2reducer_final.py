#!/usr/bin/env python
import sys
import csv
import json

current_user = None
current_rating_count = 0
userlist = {}
genreList = {}
for line in sys.stdin:
    line = line.strip()
    userid, ratingcount, receivegenrelist = line.split("\t", 2)
    genrecount = json.loads(receivegenrelist)
    ratingcount = int(ratingcount)

    if current_user == userid:
        try:
            
            userlist[userid] += ratingcount
            for genre in genrecount:
                if genre in genreList[userid]:
                        genreList[userid][genre] += genrecount[genre]
                else:
                        genreList[userid][genre] = genrecount[genre]
               
                    
        except ValueError:
            continue
    else:
        
        current_user = userid
        try:
            
            userlist[userid] = ratingcount
            for genre in genrecount:
                if userid in genreList:
                    if genre in genreList[userid]:
                        genreList[userid][genre] += genrecount[genre]
                    else:
                        genreList[userid][genre] = genrecount[genre]
                else:
                    genreList[userid] = {}
                    genreList[userid][genre] = genrecount[genre]
        except ValueError:
            continue



maxuserid = max(userlist, key = userlist.get)
mostgenre = max(genreList[maxuserid], key=genreList[maxuserid].get)
print("userid is %s\t-- Total Rating Counts:%s\t -- Most Rated Genre:%s\t - %s" % (maxuserid, userlist[maxuserid], mostgenre,genreList[maxuserid][mostgenre]))