import bottle

@bottle.route('/')
def home_page():
      return '<b> This is the home page </b>'


@bottle.route('/testpage')
def test_page():
      return 'This is the test page'

bottle.debug(True)
bottle.run(host='localhost',port=8080)
