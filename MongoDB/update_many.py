import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
scores = db.scores


print "update_one reporting for duty"

def add_reviewer_update_many():
    try:
        result = scores.update_many({} , {"$set" : { "reviewer" : "Srujan"} })
        print result.matched_count
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_many()
    


