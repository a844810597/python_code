import urllib.request

request = urllib.request.urlopen('http://www.fishc.com/')
print(request.read(300).decode('utf-8'))
