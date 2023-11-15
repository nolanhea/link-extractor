#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

response = requests.get(sys.argv[-1])
soup = BeautifulSoup(response.text, "html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))
