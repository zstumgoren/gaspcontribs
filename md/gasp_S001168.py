#!/usr/bin/env python
import urllib

from pyquery import PyQuery as pq
#import lxml.html
#import scraperwiki

BASE_URL = 'http://sarbanes.house.gov'
BIOGUIDE_ID = 'S001168'

#gasp_helper = scraperwiki.utils.swimport("gasp_helper")
#gasp = gasp_helper.GaspHelper("100cb49eec17480db65becac765a495d", BIOGUIDE_ID)

def scrape_bio():
    
    url = BASE_URL + '/free_details.asp?id=44#bio' 
    #html = scraperwiki.scrape(url)
    html =  urllib.urlopen(url).read()

    container = pq(html)('div.bodyblock span')
    content = pq(container).text()
    import pdb;pdb.set_trace()
    #gasp.add_biography(content, url=url)

def scrape_socialmedia():
    """
    html = scraperwiki.scrape(BASE_URL)
    elems = pq(html)("div.signup table td a")

    gasp.add_facebook(elems[0].attrib['href'])
    gasp.add_flickr(elems[1].attrib['href'])
    gasp.add_twitter(elems[2].attrib['href'])
    gasp.add_youtube(elems[3].attrib['href'])
    gasp.add_social_media('rss', elems[4].attrib['href'])
    """

def scrape_issues():
    """
    html = scraperwiki.scrape(BASE_URL)

    issue_re = re.compile(r'menu30057300108.addItem\("(?P<title>[\w\s/]+)", "(?P<path>.*)", "0"\);')

    for (title, path) in issue_re.findall(html):

        url = BASE_URL + path

        html = scraperwiki.scrape(url)

        container = pq(html)('div.article table.contentpaneopen td')[3]
        content = "\n\n".join(pq(elem).text() for elem in pq(container).children()[6:])

        gasp.add_issue(title, content.strip(), url=url)
    """

def scrape_offices():
    """
    url = BASE_URL + '/index.php?option=com_content&view=article&id=4104&Itemid=300138'
    html = scraperwiki.scrape(url)
    
    container = pq(html)('div.article table.contentpaneopen')[1]
    for elem in pq(container)('p')[1:]:

        content = pq(elem).text().strip()

        address_re = re.compile(r'(.*)\s+Phone:\s+([\d\s\-\(\)]+)\sFax:\s+([\d\s\-\(\)]+)')

        (address, phone, fax) = address_re.match(content).groups()

        gasp.add_office(address, phone, fax=fax, url=url)
    """

def scrape_pressreleases():
    """
    html = scraperwiki.scrape(BASE_URL + '/index.php?option=com_content&view=article&id=4093&Itemid=300128')
    
    for elem in pq(html)('div#idGtReportDisplay a'):
        
        url = BASE_URL + elem.attrib['href']

        pr_re = re.compile(r"(\w+) (\d{1,2}),(\d{4}) (.*)")
        groups = pr_re.match(pq(elem).text()).groups()
        
        date = "%s %s, %s" % groups[:-1]
        title = groups[3]

        html = scraperwiki.scrape(url)
        container = pq(html)("div.article table.contentpaneopen")[1]
        content = pq(container).text()

        gasp.add_press_release(title, date, content, url=url)
    """


def scrape_events():
    pass
    # eh, this isn't super clean
    # some of his events are at multiple locations
    # and the markup for each event varies enough to make
    # hard to scrape location addresses
    
    #html = scraperwiki.scrape(BASE_URL + '/index.php?option=com_content&view=article&id=4350&Itemid=300166')

    #for elem in pq(html)('div#idGtReportDisplay a'):
        
        #url = BASE_URL + elem.attrib['href']
        
        #events_re = re.compile(r"(\w+) (\d{1,2}),(\d{4}) (.*)")
        #groups = events_re.match(pq(elem).text()).groups()
        
        #date = "%s %s, %s" % groups[:-1]
        #title = groups[3]

        #gasp.add_event(self, title, date, location, **kwargs):

scrape_bio()
#scrape_socialmedia()
#scrape_issues()
#scrape_offices()
#scrape_pressreleases()
#scrape_events()

gasp.finish()
