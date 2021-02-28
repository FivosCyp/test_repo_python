import urllib.request
import json
import datetime
list = []
date = datetime.datetime.now()
cDay = int(date.strftime('%d'))
for i in range(1, cDay):
    list.clear()
    max = 0
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-{:02d}/2021-02-{:02d}".format(i, i)
    r = urllib.request.urlopen(url)
    drawid = r.read()
    drawid = drawid.decode()
    data = json.loads(drawid)
    for x in range(10):
        for y in range(20):
            list.append(data["content"][x]["winningNumbers"]["list"][y])
    from collections import Counter
    max = Counter(list).most_common(1)
    print(max)
