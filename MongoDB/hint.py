import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
people = db.foo


def find_test():
    query = {"a": 100 , "b": 100 , "c": 100  }
    cur = people.find(query).hint([("a",pymongo.ASCENDING)])
    try:
        for doc in cur:
            print doc
            
    except Exception as e:
        print "exception is ",type(e),e

find_test()
