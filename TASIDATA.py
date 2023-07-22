import requests
from bs4 import BeautifulSoup
url = 'https://www.saudiexchange.sa/wps/portal/saudiexchange/ourmarkets/main-market-watch/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziTR3NDIw8LAz8LVxcnA0C3bwtPLwM_I0MzMz1w1EVGAQHmAIVBPga-xgEGbgbmOlHEaPfAAdwNCCsPwpNia-7mUGgn2Ogv5G5qYFBsBG6AixOBCvA44bgxCL9gtzQCIPMgHQAVrLIOQ!!/dz/d5/L0lHSkovd0RNQUZrQUVnQSEhLzROVkUvZW4!/'
page = requests.get(url)

print(page.status_code)