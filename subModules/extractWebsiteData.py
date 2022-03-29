import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions
import validators
import tldextract

def extractDomain(url):
    if "http" in str(url) or "www" in str(url):
        parsed = tldextract.extract(url)
        parsed = parsed[1] + '.' + parsed[2]
        return parsed
    else:
        return url

def getEmailFacebook(website):
    # Parameters:  takes website url and returns filtered email and facebook links
    # Task : checks all the pages of the given domain one by one to get email and facebook link and returns when found
    # Using: `getEmailLinksFromPage(website)`, `getEmailFromPage(link)`
    # Scope: Can be used to get phone numbers from this function

    emails, links, facebook = getEmailLinksFromPage(website)
    if len(emails) == 0:
        for link in links:
            if extractDomain(website) in link and 'contact' in link.lower():                # check homepage and contact pages for this website to extract email
                print('Contact Link : ', link)
                emails = getEmailFromPage(link)
                if len(emails) > 0:
                    break
    return emails, facebook


def processURL(url, website):
    if website not in url:
        url = url.replace('/', '')
        if website[len(website) - 1] == '/':
            url = website + url
        else:
            url = website + '/' + url
    #print('Contact Link : ', url)
    return url


def getEmailLinksFromPage(URL):
    # Parameters: takes Website URL and returns email, all links, facebook link
    # Task : checks only domain page returns email, facebook if found
    # Using : getRejexEmail(page_html), FACEBOOK_REGEX
    # Exception : Typeerror occurs when url is not valid

    browser = webdriver.Chrome('C:/Users/Monir/Documents/chromedriver.exe')
    try:
        browser.get(URL)
    except exceptions.WebDriverException:
        print('Webdriver Exception for URL: ', URL)

    page_content = browser.execute_script("return document.body.innerHTML")
    page_html = BeautifulSoup(page_content, 'html.parser')

    # facebook regex
    FACEBOOK_REGEX = r"((http|https)://)?(www[.])?facebook.com/.+"
    pattern = re.compile(FACEBOOK_REGEX)
    # collects all links for this website
    links = []
    facebook = []
    for link in page_html.findAll('a'):
        url = link.get('href')
        # Preprocessing URL
        if type(url) == str:
            if 'contact' in url.lower() and 'http' not in url.lower():
                url = processURL(url, URL)

        # When type error occurs
        try:
            if validators.url(url):
                if url not in links:
                    links.append(url)
                    if re.fullmatch(pattern, url):
                        if url not in facebook:
                            facebook.append(url)
        except TypeError:
            pass

    emails = getRejexEmail(page_html)
    browser.close()
    return emails, links, facebook


def getEmailFromPage(URL):
    # Parameters : takes domain URL and returns emails
    # Task : checks a webpage and returns emails from that page
    # Using : getRejexEmail(page_html), beautifulsoup

    browser = webdriver.Chrome('C:/Users/Monir/Documents/chromedriver.exe')
    browser.get(URL)
    page_content = browser.execute_script("return document.body.innerHTML")
    page_html = BeautifulSoup(page_content, 'html.parser')
    emails = getRejexEmail(page_html)
    browser.close()
    return emails


def getRejexEmail(r):
    # Parameters: takes html.text and returns emails
    # Task : checks text and match email regex

    EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+"
    email = set()
    for re_match in re.findall(EMAIL_REGEX, r.text):
        email.add(re_match)
    return email

#***********************************************************************
# Algorithm : Get Email from a Website
# Domain name = URL
# Go to the domain and extract email from it
#
# if email not found
#	Go to all pages with that Domain
#	try ro extract email from these pages until found

u = 'https://popalock.ca/edmonton/'
emails, facebook = getEmailFacebook(u)
print('Emails: ', emails)
print('Facebook : ', facebook)
#***********************************************************************

#print(validators.url(u))