import requests
import json
import time
import urllib.request, urllib.parse, urllib.error
from collections import defaultdict

biblegatewayURL =  "https://api.biblegateway.com/2/request_access_token?username=\"sloporto@asi-test.com\"&password=\"Tslasibgw1!\""
b = requests.get(biblegatewayURL)
theJSON = json.loads(b.content)
time.sleep(1)