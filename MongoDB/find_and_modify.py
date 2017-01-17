import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
counters = db.counters


print "find and modify reporting for duty"

def add_reviewer_update_one(name):
    try:
        counter = counters.find_one_and_update( filter = {'type': name} , update = { '$inc' : {'value' : -1}  } , upsert = True , return_document = pymongo.ReturnDocument.AFTER  )
        counter_value = counter['value']
        return counter_value

        
        
    except Exception as e:
        print "exception is " , type(e) , e

print add_reviewer_update_one('uid')
print add_reviewer_update_one('uid')
print add_reviewer_update_one('uid')
    


