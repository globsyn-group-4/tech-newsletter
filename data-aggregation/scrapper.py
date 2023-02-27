import requests
from bs4 import BeautifulSoup
import json

urls='''https://medium.com/airbnb-engineering/latest
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
https://medium.com/@pinterest_engineering
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
https://medium.com/picsart-engineering/latest'''


blogs = []

for url in urls.split('\n'):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.content, 'html.parser')
  articlelist = soup.find_all(attrs={'class': 'postArticle'})
  for article in articlelist:
    blog = dict()
    blog['publishedDate'] = article.find('time').get('datetime')
    blog['header'] = article.find('h3').text
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

    #print(json.dumps(blog, indent=4))
    blogs.append(blog)

out_file = open("blogs.json", "w")   
json.dump(blogs, out_file, indent = 2)