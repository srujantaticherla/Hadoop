import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
score = db.scores

def find_one_test():
    try:
        query = {"student" : 11}
        doc = score.find_one(query)
        print doc
    except Exception as e :
        print "exception is ",type(e) , e

find_one_test()

    
