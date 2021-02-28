import urllib.request
import json
filename = input('Give the name of the file or the path:')
f = open(filename,'r')
dict = json.loads(f.read())
f.close()
l = len(dict)
kleidi = list(dict.keys())
timi = list(dict.values())
for i in range (l):
    str = kleidi[i]
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + str + "&tsyms=EUR"
    r = urllib.request.urlopen(url)
    page = r.read()
    page = page.decode()
    dict2 = json.loads(page)
    op = str + "in euro:"
    poso = dict2[str]["EUR"] * timi[i]
    print(op,poso)
