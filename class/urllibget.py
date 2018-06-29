import urllib.request


url = 'https://www.lagou.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
   html_doc = response.read()


with open('lagou.html', 'wb') as la:
    la.write(html_doc)


