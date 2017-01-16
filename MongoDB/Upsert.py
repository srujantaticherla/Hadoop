import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
things = db.things


print "update_one reporting for duty"

def add_reviewer_update_many():
    try:
        things.drop()
        things.update_one({'thing':'apple'} , { '$set' : { 'color' :'red'  }  } , upsert = True)
        things.update_many({'thing':'banana'} , { '$set' : { 'color' :'yellow'  }  } , upsert = True)
        things.replace_one({'thing':'pear'} , { 'color' :'red'  }  , upsert = True)

        apple = things.find_one({'thing':'apple'})
        print apple
        banana = things.find_one({'thing':'banana'})
        print banana

        pears = things.find_one({'thing':'pear'})
        print pears
        
        
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_many()
    


