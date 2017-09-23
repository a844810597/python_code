import urllib.request
import chardet

response = urllib.request.urlopen('http://www.fishc.com/')
html = response.read()

print(chardet.detect(html))
