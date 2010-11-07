import HTMLParser
import login
import urllib2

ROOT_URL = 'http://www.chipublib.org'
SUMMARY_URL = 'http://www.chipublib.org/mycpl/summary'

class RenewLinkParser(HTMLParser.HTMLParser, object):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.renew_links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href' and 'renew' in value:
                    self.renew_links.append(value)

def getSummaryPage(opener):
    request = urllib2.Request(SUMMARY_URL, None, login.HEADERS)
    response = opener.open(request)
    return response.read()

def getRenewLinks(page):
    parser = RenewLinkParser()
    parser.feed(page)
    return parser.renew_links

def renewBooks():
    opener = login.login()
    page = getSummaryPage(opener)
    renew_links = getRenewLinks(page)
    for renew_link in renew_links:
        renew_link = ROOT_URL + renew_link
        request = urllib2.Request(renew_link, None, login.HEADERS)
        opener.open(request)

if __name__ == '__main__':
    renewBooks()
