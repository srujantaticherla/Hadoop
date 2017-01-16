import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
scores = db.scores


print "update_one reporting for duty"

def add_reviewer_update_many():
    try:
        score = scores.find_one()
        print "before change" , score
        score['reviewer'] = 'Srujan'

        record_id = score['_id']
        scores.replace_one({'_id': record_id} , score)
        score = scores.find_one({'_id' : record_id})
        print "after change" , score

        
        
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_many()
    


