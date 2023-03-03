from requests import get, Request
from bs4 import BeautifulSoup, ResultSet, Tag
import json
from dateutil.parser import parse
from html import unescape
from typing import List, Dict
from enum import Enum


TEXT_ATTRIBUTE="text"

class METADATA_CONTAINER_NAMES(str, Enum):
  HEADER="headerContainer"
  URL="urlContainer"
  DATE="publishedDateContainer"

class BLOG_METADATA_KEYS(str, Enum):
  HEADER="header"
  URL="articleUrl"
  DATE="publishedDate"


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
      blogs.append(blog)
  return blogs

def get_key_from_container_name(container:str)->str:
  match container:
    case METADATA_CONTAINER_NAMES.HEADER:
      return BLOG_METADATA_KEYS.HEADER.value
    case METADATA_CONTAINER_NAMES.DATE:
      return BLOG_METADATA_KEYS.DATE.value
    case _:
      return BLOG_METADATA_KEYS.URL.value

def parse_data_using_schema(
  article_element: Tag,
  tag_name: str = None,
  selector_name: str = None,
  selector_value: str = None,
  extraction_attribute_name: str = None
) -> str:
  data_element = article_element.find(tag_name, attrs={selector_name:selector_value})
  if data_element:
    if extraction_attribute_name == TEXT_ATTRIBUTE:
      return data_element.text if data_element.text else ""
    data:str = data_element.get(extraction_attribute_name)
    return data if data else ""
  return ""


def extract_schema_attributes(schema: dict, container_name:str):
  article_container:Dict = schema.get(container_name)
  tag_name:str=article_container.get("tagName")
  selector_name:str=article_container.get("selectorName")
  selector_value:str=article_container.get("selectorValue")
  extraction_attribute_name:str=article_container.get("extractionAttributeName")
  return tag_name, selector_name, selector_value, extraction_attribute_name

def form_blog_meta_data(
  article_element: Tag,
  schema:dict,
  schema_keys: List[str]
) -> Dict:
  blog=dict()
  for i in range(4,1,-1):
    tag_name, selector_name, selector_value, extraction_attribute_name = extract_schema_attributes(
      schema=schema, 
      container_name=schema_keys[i]
    )
    blog[get_key_from_container_name(schema_keys[i])]=parse_data_using_schema(
      tag_name=tag_name,
      article_element=article_element,
      selector_value=selector_value,
      selector_name=selector_name,
      extraction_attribute_name=extraction_attribute_name
    )
  return blog

def scrape_non_medium_articles(schemas: List[dict]) -> List[dict]:
  blogs: List[dict] = []
  for schema in schemas:
    schema_keys: List[str] = list(schema.keys())
    soup=get_html_for_url(schema.get(schema_keys[0]))
    tag_name, selector_name, selector_value, _ = extract_schema_attributes(
      schema=schema, 
      container_name=schema_keys[1]
    )
    article_elements:ResultSet = soup.find_all(
      name=tag_name, 
      attrs={
        selector_name:selector_value
      }
    )
    for article_element in article_elements:
      blog=form_blog_meta_data(
        article_element=article_element,
        schema=schema,
        schema_keys=schema_keys
      )
      blogs.append(blog)
      
  return blogs


def parse_json_file(filename: str) -> List[Dict]:
  with open(filename) as json_file:
    data: List[Dict] = json.load(json_file)
    json_file.close()
    return data


blog_schemas = parse_json_file("blogSchema.json")
blogs=scrape_non_medium_articles(blog_schemas)
medium_blogs=scrape_medium_articles(links)
blogs.extend(medium_blogs)

out_file = open("blogs.json", "w")   
json.dump(blogs, out_file, indent = 2)