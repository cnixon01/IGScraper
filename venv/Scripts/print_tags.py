from bs4 import BeautifulSoup
import urllib3
import certifi

#url = urlopen("http://www.python.org")
#content = url.read()
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
req = http.request('GET', 'http://www.python.org')
content = req.read()

soup = BeautifulSoup(content)

links = soup.findAll("a")
for href in links:
    print(href)