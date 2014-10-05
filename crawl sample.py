# The Web Crawler...

# it's going to be recursive and search for href's on a depth first search

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

visited = []

# same collector from last class
class Collector(HTMLParser):
    '''collector based on the superclass parser'''

    def __init__(self, url):
        
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        '''finds starting tags and appends them if found'''

        if tag == 'a':
            # anchor tells us we are starting at href
            for attr in attrs:
                
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    
                    if absolute[:4] == 'http':
                        self.links.append(absolute)
                        

    def getLinks(self):
        return self.links

def crawl(url):
    '''keep crawlin, crawlin..'''
    global visited

    visited.append(url)

    links = analyze(url)

    for link in links:
        if link not in visited:
            try:
                crawl(link)
            except:
                pass

def analyze(url):
    '''Analyze the Target!!!!!!'''
    print('\n\nVisting: ', url)

    content = urlopen(url).read().decode()

    collector = Collector(url)
    collector.feed(content)

    urls = collector.getLinks()
    

    # think about writing a getData() and frequency method..
    #content = collector.getData()

    # frquency of everything in the new data
    #frequency(content)

    for link in urls:
        print("{:45}{:10}".format(url, link))

    return urls


url = 'http://www.reddit.com'

# get ready for a huge output...
crawl(url)
