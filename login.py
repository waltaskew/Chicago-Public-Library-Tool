"""Functions to login in to the CPL website.
"""

import cookielib
import ConfigParser
import urllib
import urllib2

LOGIN_FILE = 'login.ini'
LOGIN_SECTION = 'login'
LOGIN_URL = 'https://www.chipublib.org/mycpl/login/'
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
HEADERS = {
        'User-Agent' : USER_AGENT
}

def get_login_info():
    """Read login credentail from a config file.
    """
    config = ConfigParser.RawConfigParser()
    config.read(LOGIN_FILE)
    card = config.get(LOGIN_SECTION, 'card_number')
    zip_code = config.get(LOGIN_SECTION, 'zip')
    return card, zip_code

def get_opener():
    """Return a url opener that handles cookies.
    """
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    return opener

def login():
    """Login to the My CPL page.  Returns an opener
    that can make requests on other CPL pages while 
    logged in as a user.
    """
    opener = get_opener()
    card, zip_code = get_login_info()
    values = {
            'loginButton': 'Login',
            'loginButton.x': 58,
            'loginButton.y': 13,
            'myCplLogin': 'Login',
            'patronId': card,
            'zipCode': zip_code,
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(LOGIN_URL, data, HEADERS)
    opener.open(req)
    return opener
