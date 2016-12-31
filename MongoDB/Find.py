import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
people = db.scores


def find_test():
    query = {"score": { '$gt':  50}  }
    sanity =0
    cur = people.find(query).sort([("student",pymongo.ASCENDING),("score",pymongo.DESCENDING)]).limit(10).skip(4)
    try:
        for doc in cur:
            print doc
            sanity += 1
            #if (sanity > 10):
            #   break
    except Exception as e:
        print "exception is ",type(e),e

find_test()
