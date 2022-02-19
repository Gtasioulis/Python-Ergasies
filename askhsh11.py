from urllib.request import Request, urlopen   #Άσκηση 11 p21162
import pandas as pd 
from scipy.stats import entropy 
req1 = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data1 = urlopen(req1).read()
a = str(data1)
b = a.split(",")
c = str(b[0])
d = c.split(":")
e = d[1]
f = a.split('"randomness":',1)
g = str(f[1])
h = g.split(",",1)
list = [ ]
for d in f[0][1:-1]:
    list.append(f)
for i in range(19):
    e = int(e)-1
    req2 =  Request('https://drand.cloudflare.com/public/'+str(e), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data2 = urlopen(req2).read()
    m = str(data2)
    n = m.split('"randomness":',1)
    o = str(n[1])
    p = o.split(",",1)
    for f in p[0][1:-1]:
        list.append(f)
list = pd.Series(list)
last = entropy(list.value_counts(),base=2)
print("Η εντροπία είναι: ",last)







