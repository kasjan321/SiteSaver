##Created by kasjan321
import urllib3
import sys
import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("site")
args = parser.parse_args()
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
http = urllib3.PoolManager(10, headers=user_agent)
request = http.request('GET', args.site)
output = request.data.decode('utf-8')
with open("output.html", "w") as file:
    file.write(output)
print('DONE')


