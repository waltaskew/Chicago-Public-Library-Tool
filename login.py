import cookielib
import ConfigParser
import urllib
import urllib2

LOGIN_FILE = 'login.ini'
LOGIN_SECTION = 'login'
LOGIN_URL = 'http://www.chipublib.org/mycpl/login/'
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
HEADERS = {
        'User-Agent' : USER_AGENT
}

def getLoginInfo():
    config = ConfigParser.RawConfigParser()
    config.read(LOGIN_FILE)
    card = config.get(LOGIN_SECTION, 'card_number')
    zip = config.get(LOGIN_SECTION, 'zip')
    return card, zip

def getOpener():
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    return opener

def login():
    opener = getOpener()
    card, zip = getLoginInfo()
    values = {
            'loginButton': 'Login',
            'loginButton.x': 45,
            'loginButton.y': 19,
            'myCplLogin': 'Login',
            'patronId': card,
            'zipCode': zip,
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(LOGIN_URL, data, HEADERS)
    opener.open(req)
    return opener
