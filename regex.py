import urllib
import re

web = 'yahoo google cnn msn lagosonrails andela 2u'.split()
path = re.compile('<title>.*</title>')
for site in web:
    try:
        url = urllib.urlopen('http://' + site + '.com')
    except:
        url = urllib.request.urlopen('http://' + site + '.com')
    title = url.read()
    text = re.findall(path, title)
    print text[0]
