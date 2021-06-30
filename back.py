'''Backend Program - URL Shortener by DJ Harshit'''

# Importing the modules
import json
import random

# Downloading and importing requests module
try:
    import requests
except:
    import sys
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
finally:
    import requests

# Get one api from the list
with open('api.txt') as f:
    tkns = f.readlines()
    tkn = random.choice(tkns).strip()
hdrs = {'Authorization': f'Bearer {tkn}'}

# Class for creating short url
class Short_Url():
    def __init__(self, site):
        self.site = site

    # Check if long url has http:// in it 
    def check(self):
        if 'http://' in self.site or 'https://' in self.site:
            pass
        else:
            self.site = 'https://' + self.site

    # Get the response after request is sent
    def generate(self):
        global out
        dat = {"long_url": self.site}
        dat = json.dumps(dat)
        res = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=hdrs, data=dat)
        out = json.loads(res.text)

    # Send the short url to first.py
    def send_url(self):
        return out['link']