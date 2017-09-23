import urllib.request

req= urllib.request.Request('http://placekitten.com/g/500/700')
response = urllib.request.urlopen(req)
cat_img = .response.read()

with open('E:\\cat_500_700.JPG', 'wb') as f:
    f.write(cat_img)
