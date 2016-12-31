import pymongo , bottle

from pymongo import MongoClient

@bottle.route('/')

def index():
    connection = MongoClient('localhost',27017)
    db = connection.test
    name = db.names
    for items in name.find():
      return '<b> Hello %s </b>!'  %items['name']

bottle.run(host='localhost',port=8082)
