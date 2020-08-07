#!/usr/bin/env python
import sys
import csv
import json
import math
#import numpy as np
current_genre = None
current_rating_sum = 0
current_rating_count = 0

median_rating = 0.0
genreratingInfo ={}
for line in sys.stdin:
    line = line.strip()
    genre, ratingString, eachratingcount = line.split("\t", 2)
    ratingInfo = json.loads(ratingString)
    eachratingInfo = json.loads(eachratingcount)
    if current_genre == genre:
        try:
            current_rating_sum += ratingInfo["total_rating"]
            current_rating_count += ratingInfo["total_count"]
            for rating in eachratingInfo:
                if genreratingInfo[genre][rating]:
                    genreratingInfo[genre][rating] += eachratingInfo[rating]
                else:
                    genreratingInfo[genre][rating] = eachratingInfo[rating]
        except ValueError:
            continue
    else:
        if current_genre:
            median_count = 0
            ratinglist = []
            ratingcountList =[0.0]
            total_std = 0.0
            rating_average = current_rating_sum / current_rating_count
            #std
            for ratingcount in sorted(genreratingInfo[current_genre]):
                #total_std += (float(ratingcount) - rating_average) * (float(ratingcount) - rating_average) * genreratingInfo[current_genre][ratingcount]
                #print("current_genre",current_genre,"ratingcount", ratingcount,"rating_average",rating_average,"genreratingInfo[current_genre][ratingcount]",genreratingInfo[current_genre][ratingcount],"total_std",total_std)
                    
                total_std += math.pow( float(ratingcount) - rating_average,2) * genreratingInfo[current_genre][ratingcount]
            #std



            #  ***********midain ************************
            median = current_rating_count / 2 
            if current_rating_count % 2 != 0:
                median += 0.5
            else:
                median += 1
            
            #print("current_genre",current_genre,"median",median,'current_rating_count',current_rating_count)
            for ratingcount in sorted(genreratingInfo[current_genre]):
                    #print("current_genre",current_genre,"rating",ratingcount)
                    
                    ratinglist.append(ratingcount)
                  
                    median_count += genreratingInfo[current_genre][ratingcount]
                   
                    if median_count >= median and current_rating_count % 2 != 0:
                        median_rating = ratingcount
                        ratingcountList.append(median_count)
                        break;
                    if median_count >= median and current_rating_count % 2 == 0:
                        median -= 1
                        
                        if median - ratingcountList[-1] < 1:
                            index = ratinglist.index(ratingcount)
                            
                            median_rating  = (float(ratinglist[index-1]) + float(ratinglist[index])) / 2.0
                            ratingcountList.append(median_count)
                            break;
                        else:
                            median_rating = ratingcount
                            ratingcountList.append(median_count)
                            break;
                    ratingcountList.append(median_count)
            #  ***********midain end ************************
            # std
            if current_rating_count == 1:
              current_rating_count = 2
            std = math.sqrt(total_std / (current_rating_count -1 ))   
            #print("total_std",total_std,"total_count",current_rating_count)
            if current_genre.find("no") == -1:        
                print("Genre is %-15s\tMean is %-20s\tMedian is %-10s\tStandard Deviation is %s" % (current_genre, rating_average, median_rating,std))
        current_genre = genre
        try:
            current_rating_sum = ratingInfo["total_rating"]
            current_rating_count = ratingInfo["total_count"]
            genreratingInfo[genre] = {}
            for rating in eachratingInfo:
                genreratingInfo[genre][rating] = eachratingInfo[rating]
        except ValueError:
            continue

if current_genre == genre:
    median_count = 0
    ratinglist = []
    total_std = 0.0
    rating_average = current_rating_sum / current_rating_count
    #std
    for ratingcount in sorted(genreratingInfo[current_genre]):
        #total_std += (float(ratingcount) - rating_average) * (float(ratingcount) - rating_average) * genreratingInfo[current_genre][ratingcount]
        #print("current_genre",current_genre,"ratingcount", ratingcount,"rating_average",rating_average,"genreratingInfo[current_genre][ratingcount]",genreratingInfo[current_genre][ratingcount],"total_std",total_std)
                    
        total_std += math.pow( float(ratingcount) - rating_average,2) * genreratingInfo[current_genre][ratingcount]
    #std

    median = current_rating_count / 2 
    if current_rating_count % 2 != 0:
                median += 0.5
    else:
                median += 1
            
    #print("current_genre",current_genre,"median",median,'current_rating_count',current_rating_count)
    for ratingcount in sorted(genreratingInfo[current_genre]):
                    #print("current_genre",current_genre,"rating",ratingcount)
                    
                    ratinglist.append(ratingcount)
                    median_count += genreratingInfo[current_genre][ratingcount]
                    if median_count >= median and current_rating_count % 2 != 0:
                        median_rating = ratingcount
                        break;
                    if median_count >= median and current_rating_count % 2 == 0:
                        median -= 1
                        if median - ratingcountList[-1] < 1:
                            index = ratinglist.index(ratingcount)
                           
                            median_rating  = (float(ratinglist[index-1]) + float(ratinglist[index])) / 2.0
                            break;
                        else:
                            median_rating = ratingcount
                            break;
    if current_rating_count == 1:
              current_rating_count = 2
    std = math.sqrt(total_std / (current_rating_count -1 ))   
    #print("total_std",total_std,"total_count",current_rating_count)  
    if current_genre.find("no") == -1:
        print("Genre is %-15s\tMean is %-20s\tMedian is %-10s\tStandard Deviation is %s" % (current_genre, rating_average, median_rating,std))
