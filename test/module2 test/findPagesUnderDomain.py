# Find and Parse Sitemaps to Create List of all website's pages
from usp.tree import sitemap_tree_for_homepage
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import validators


def getEmailFacebook(website):
    emails, links, facebook = getEmailLinksFromPage(website)
    if len(emails) == 0:
        for link in links:
            if website in link:                                   # check all pages for this website to extract email
                emails = getEmailFromPage(link)
                if len(emails) > 0:
                    break
    return emails, facebook


def getEmailLinksFromPage(URL):
    browser = webdriver.Chrome('C:/Users/Monir/Documents/chromedriver.exe')
    browser.get(URL)
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
        if validators.url(url):
            if url not in links:
                links.append(url)
                if re.fullmatch(pattern, url):
                    if url not in facebook:
                        facebook.append(url)

    emails = getRejexEmail(page_html)
    browser.close()
    return emails, links, facebook


def getEmailFromPage(URL):
    browser = webdriver.Chrome('C:/Users/Monir/Documents/chromedriver.exe')
    browser.get(URL)
    page_content = browser.execute_script("return document.body.innerHTML")
    page_html = BeautifulSoup(page_content, 'html.parser')
    emails = getRejexEmail(page_html)
    browser.close()
    return emails


def getRejexEmail(r):
    # extract email from *Webpage.text*
    EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+"
    email = set()
    for re_match in re.findall(EMAIL_REGEX, r.text):
        email.add(re_match)
    return email


def getPagesFromSitemap(fullDomain):
    listPagesRaw = []
    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPagesRaw.append(page.url)
    return listPagesRaw


# Go through List Pages Raw output a list of unique pages links
def getListUniquePages(listPagesRaw):
    listPages = []
    for page in listPagesRaw:
        if page in listPages:
            pass
        else:
            listPages.append(page)
    return listPages

#***********************************************************************
# Algorithm : Get Email from a Website
# Domain name = URL
# Go to the domain and extract email from it
#
# if email not found
#	Go to all pages with that Domain
#	try ro extract email from these pages until found

#'https://mrlockman.ca/'
#emails, facebook = getEmailFacebook('https://mrlockman.ca/')
#print('Emails: ', emails)
#print('Facebook : ', facebook)
#***********************************************************************