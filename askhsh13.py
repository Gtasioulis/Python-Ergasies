from urllib.request import Request, urlopen #Άσκηση 13 p21162
import json
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
a= json.loads(data)
telgyr = a["round"]
for gyr in range(telgyr, telgyr-100, -1):
	req= Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
	data= urlopen(req).read()
	a=json.loads(data)
	randomness= a["randomness"]
#Χωρίζω σε δυάδες 16δικών
diaxorismos = []
k  = 2
for index in range(0, len(randomness), k):
	diaxorismos.append(randomness[index : index + k])
# Μετατροπή 16δικών σε ακεραίους 
for i in range(0, len(diaxorismos)):
	diaxorismos[i] = int(diaxorismos[i],16)
#Κάνω modulo 80
for i in range(0, len(diaxorismos)):
	diaxorismos[i] = diaxorismos[i] % 80
#κρατάω το καθένα μια φορά
diaxorismos = list(set(diaxorismos)) 
req= Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data= urlopen(req).read()
kino1 = json.loads(data)
arkino=[]
kino2 = kino1['last']["winningNumbers"]['list']
for i in kino2:
	arkino.append(i)
#Έλεγχος αριθμών με αυτών του Κίνο
for i in range(0, len(diaxorismos)):
	for j in range(0, len(arkino)):
	    if diaxorismos[i] == arkino[j]:
	        print("Οι αριθμοί που θα κληρονόντουσαν στην τελευταία κλήρωση του ΚΙΝΟ είναι: ", diaxorismos[i])
