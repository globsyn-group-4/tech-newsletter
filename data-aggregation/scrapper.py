from requests import get, Request
from bs4 import BeautifulSoup, ResultSet
import json
from dateutil.parser import parse
from html import unescape
from typing import List


links = '''https://medium.com/airbnb-engineering/latest
https://netflixtechblog.com/latest
https://medium.com/groupon-eng/latest
https://tech.groww.in/latest
https://engineering.razorpay.com/latest
https://bytes.swiggy.com/latest
https://blog.dream11engineering.com/latest
https://medium.com/smallcase-engineering/latest
https://tech.makemytrip.com/latest
https://blog.flipkart.tech/latest
https://engineering.cred.club/latest
https://medium.com/walmartglobaltech/latest
https://techatmpl.com/
https://tech.instacart.com/latest
https://medium.com/gojekengineering/latest
https://canvatechblog.com/latest
https://medium.com/udemy-engineering/latest
https://medium.com/vimeo-engineering-blog/latest
https://medium.com/paypal-tech/latest
https://engg.glance.com/latest
https://tech.urbancompany.com/latest
https://medium.com/intuit-engineering/latest
https://medium.com/motive-eng/latest
https://engineering.tableau.com/latest
https://medium.com/meesho-tech/latest
https://medium.com/better-practices/latest
https://medium.com/expedia-group-tech/latest
https://medium.com/myntra-engineering/latest
https://medium.engineering/latest
https://medium.com/pinterest-engineering/latest
https://tech.buzzfeed.com/latest
https://medium.com/naukri-engineering/latest
https://blog.hotstar.com/latest
https://medium.com/engineering-housing/latest
https://medium.com/1mgofficial/latest
https://tech.bigbasket.com/latest
https://medium.com/brainly/latest
https://medium.com/glassdoor-engineering/latest
https://engineering.udacity.com/latest
https://medium.com/udemy-engineering/latest
https://medium.com/blackrock-engineering/latest
https://medium.com/harness-engineering/latest
https://medium.com/airteldigital/latest
https://medium.com/freshworks-engineering-blog/latest
https://medium.com/adidoescode/latest
https://medium.com/decathlontechnology/latest
https://medium.com/quantumblack/latest
https://medium.com/tata-cliq-tech-blog/latest
https://medium.com/picsart-engineering/latest
https://medium.com/payu-engineering/latest
https://medium.com/tinder/latest
https://medium.com/bumble-tech/latest
https://blog.gofynd.com/latest
https://medium.com/hevo-data-engineering/latest
https://we-are.bookmyshow.com/latest'''


def get_html_for_url(url: str) -> BeautifulSoup:
  resp: Request  = get(url, verify=False)
  soup: BeautifulSoup = BeautifulSoup(resp.content, 'html.parser')
  return soup


def scrape_medium_articles(urls: List[str]) -> List[dict]:
  blogs: List[dict] = []
  for url in urls.split('\n'):
    soup=get_html_for_url(url)
    articlelist:ResultSet = soup.find_all(attrs={'class': 'postArticle'})
    for article in articlelist:
      blog = dict()
      blog['publishedDate'] = parse(
        article.find('time').get('datetime')).strftime("%d/%m/%Y")
      blog['header'] = unescape(article.find('h3').text)
      blog['subHeader'] = article.find('h4').text if article.find('h4') else ""
      blog['blogName'] = article.find(
        'a',
        attrs={
          'class':
          'ds-link ds-link--styleSubtle link--darken link--accent u-accentColor--textNormal'
        }).text
      blog['articleUrl'] = article.find('a',
                                        attrs={
                                          'class': 'link link--darken'
                                        }).get('href')
      blog['author'] = article.find(
        'a',
        attrs={
          'class':
          'ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken'
        }).text
      #print(json.dumps(blog, indent=4))
      #print(blog)
      blogs.append(blog)
  return blogs


blogs=scrape_medium_articles(links)

out_file = open("blogs.json", "w")   
json.dump(blogs, out_file, indent = 2)