import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.video
movieDetails = db.movieDetails


print "Get the records that have Sweden in the 2nd place"

def add_reviewer_update_many():
    try:
        print "find the target records where Sweden is in 2nd place"
        cursor = db.movieDetails.find({"countries" : "Sweden" , "$where" : "this.countries.length >=2" } ,{ "countries":1 })
        
        for item in cursor:
            record = item['countries']
            #print record
            #print record[1]
            if record[1] == 'Sweden':
               print record
                     
            #if record[1] is not None:
             # print record

            
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_many()
    


