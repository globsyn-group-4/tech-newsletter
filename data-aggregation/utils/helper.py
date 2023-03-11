import json
from typing import List, Dict
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get, Request


def parse_json_file(filename: str) -> List[Dict]:
  with open(filename) as json_file:
    data: List[Dict] = json.load(json_file)
    json_file.close()
    return data

def get_html_for_url(url: str) -> BeautifulSoup:
  resp: Request  = get(url)
  soup: BeautifulSoup = BeautifulSoup(resp.content, 'html.parser')
  return soup

def get_clean_link(link: str) -> str:
  return urlparse(link)._replace(query=None).geturl()