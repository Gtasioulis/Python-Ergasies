# _A__B__C___D___E__F__G__H_    Σκακιέρα 8*8                            Άσκηση 8 p21162
#|__|__|__|___|___|__|__|___|8   
#|__|__|__|___|___|__|__|___|7
#|__|__|__|___|___|__|__|___|6
#|__|__|__|___|___|__|__|___|5
#|__|__|__|___|___|__|__|___|4
#|__|__|__|___|___|__|__|___|3
#|__|__|__|___|___|__|__|___|2
#|__|__|__|___|___|__|__|___|1                       

paikt1 = 0 #λευκός πύργος
paikt2 = 0 # μαύρος αξιωματικός 
i = 0
arxthesh1 = ["A","B","C","D","E","F","G","H"] #λίστα που χρησιμοποιείται για την τοποθέτηση των πιονιών στις αρχικές τους θέσεις 
arxthesh2 = [1,2,3,4,5,6,7,8] #λίστα που χρησιμοποιείται για την τοποθέτηση των πιονιών στις αρχικές τους θέσεις
bhm = [1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7]
bhmaks = ["aristera","deksia"]
bhmpyr=["katheta","orizontia"]
import random
while i<100 :
    i += 1
    pyr = [" ",0]
    aks = [" ",0]
    pyr[0] = random.choice(arxthesh1)
    pyr[1] = random.choice(arxthesh2)
    aks[0] = random.choice(arxthesh1)
    aks[1] = random.choice(arxthesh2)
    done = False
    seira = 1 # 1=παίζει ο άσπρος, 2= παίζει ο μαύρος(Βάζω 1 γιατί τα άσπρα πάντα παίζουν πρώτασ)
    while done == False:
        if seira==1:
             seira = 2
             thesh1 = random.choice(bhmpyr)
             thesh2 = random.choice(bhm)
             if thesh1=="katheta":
                 if pyr[1]+thesh2>8:
                     pyr[1] = 8
                 elif pyr[1]+thesh2<=0:
                     pyr[1] = 1
                 else :
                     pyr[1] += thesh2
             else :
                 k = ord(pyr[0])
                 if k+thesh2>72:
                     pyr[0] = "H"
                 elif k+thesh2<=64:
                     pyr[0] = "A"
                 else:
                     k += thesh2
                     pyr[0] = chr(k)
             if aks[1]==pyr[1] and aks[0]==pyr[0]:
                         done = True
                         paikt1 += 1
             
        else:
            seira = 1
            thesh1 = random.choice(bhmaks)
            thesh2 = random.choice(bhm)
            k = ord(aks[0])
            if thesh1=="aristera": 
              if aks[0]!="A":
                if thesh2>0:
                    a = k-thesh2 #a=βοηθητική μεταβλητή για να γίνει σωστά η προσθαφαίρεση είτε είναι θετικός είτε αρνητικός 
                else:
                    a = k+thesh2
                if aks[1]+thesh2>8:
                  while aks[1]<8 and aks[0]!="A":
                    aks[1] += 1
                    k -= 1
                    aks[0] = chr(k)   
                elif aks[1]+thesh2<0:
                  while aks[1]>1  and aks[0]!="A":
                    aks[1] -= 1
                    k -= 1
                    aks[0] = chr(k)
                else:
                  while thesh2>0 and aks[0]!="A" and aks[1]<8:
                        thesh2 -= 1
                        k -= 1
                        aks[1] += 1
                        aks[0] = chr(k)
                  while thesh2<0 and aks[0]!="A" and aks[1]>1:
                        thesh2 += 1
                        k -= 1
                        aks[1] -= 1
                        aks[0] = chr(k)
            else: 
              if aks[0]!="H":
                if thesh2>0:
                    a = k+thesh2
                else:
                    a = k-thesh2
                if aks[1]+thesh2>8:
                  while aks[1]<8 and aks[0]!="H":
                    aks[1] += 1
                    k += 1
                    aks[0] = chr(k)
                elif aks[1]+thesh2<0 :
                  while aks[1]>1 and aks[0]!="H":
                    aks[1] -= 1
                    b = aks[1]-1
                    k += 1
                    aks[0] = chr(k)
                else: 
                  while thesh2>0 and aks[0]!="H" and aks[1]<8:
                        thesh2 -= 1
                        k += 1
                        aks[1] += 1
                        aks[0] = chr(k)
                     
                  while thesh2<0 and aks[0]!="H" and aks[1]>1:
                        thesh2 += 1
                        k += 1
                        aks[1] -= 1
                        aks[0] = chr(k)
            if aks[1]==pyr[1] and aks[0]==pyr[0]:
                         done = True
                         paikt2 += 1
print("Τα αποτελέσματα των 100 γύρων στην σκακιέρα 8*8 είναι: Παίκτης1(Λευκός Πύργος): ",paikt1,",  Παίκτης2(Μαύρος Αξιωματικός): ",paikt2)
print(" ")

# _A__B__C___D___E__F__G_    Σκακιέρα 7*7
#|__|__|__|___|___|__|__|7
#|__|__|__|___|___|__|__|6
#|__|__|__|___|___|__|__|5
#|__|__|__|___|___|__|__|4
#|__|__|__|___|___|__|__|3
#|__|__|__|___|___|__|__|2
#|__|__|__|___|___|__|__|1 
paikt1 = 0 #λευκός πύργος
paikt2 = 0 # μαύρος αξιωματικός 
i = 0
arxthesh1 = ["A","B","C","D","E","F","G"] #λίστα που χρησιμοποιείται για την τοποθέτηση των πιονιών στις αρχικές τους θέσεις 
arxthesh2 = [1,2,3,4,5,6,7] #λίστα που χρησιμοποιείται για την τοποθέτηση των πιονιών στις αρχικές τους θέσεις
bhm = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
bhmaks = ["aristera","deksia"]
bhmpyr=["katheta","orizontia"]
import random
while i<100:
    i += 1
    pyr = [" ",0]
    aks = [" ",0]
    pyr[0] = random.choice(arxthesh1)
    pyr[1] = random.choice(arxthesh2)
    aks[0] = random.choice(arxthesh1)
    aks[1] = random.choice(arxthesh2)
    done = False
    seira = 1 # 1=παίζει ο άσπρος, 2= παίζει ο μαύρος(Βάζω 1 γιατί τα άσπρα πάντα παίζουν πρώτασ)
    while done == False:
        if seira==1:
             seira = 2
             thesh1 = random.choice(bhmpyr)
             thesh2 = random.choice(bhm)
             if thesh1=="katheta":
                 if pyr[1]+thesh2>7:
                     pyr[1] = 7
                 elif pyr[1]+thesh2<=0:
                     pyr[1] = 1
                 else :
                     pyr[1] += thesh2
             else :
                 k = ord(pyr[0])
                 if k+thesh2>71:
                     pyr[0] = "G"
                 elif k+thesh2<=64:
                     pyr[0] = "A"
                 else:
                     k += thesh2
                     pyr[0] = chr(k)
             if aks[1]==pyr[1] and aks[0]==pyr[0]:
                         done = True
                         paikt1 += 1
             
        else:
            seira = 1
            thesh1 = random.choice(bhmaks)
            thesh2 = random.choice(bhm)
            k = ord(aks[0])
            if thesh1=="aristera": 
              if aks[0]!="A":
                if thesh2>0:
                    a = k-thesh2 #a=βοηθητική μεταβλητή για να γίνει σωστά η προσθαφαίρεση είτε είναι θετικός είτε αρνητικός 
                else:
                    a = k+thesh2
                if aks[1]+thesh2>7:
                  while aks[1]<7 and aks[0]!="A":
                    aks[1] += 1
                    k -= 1
                    aks[0] = chr(k)   
                elif aks[1]+thesh2<0:
                  while aks[1]>1 and aks[0]!="A":
                    aks[1] -= 1
                    k -= 1
                    aks[0] = chr(k)
                else:
                  while thesh2>0 and aks[0]!="A" and aks[1]<7:
                        thesh2 -= 1
                        k -= 1
                        aks[1] += 1
                        aks[0] = chr(k)
                  while thesh2<0 and aks[0]!="A" and aks[1]>1:
                        thesh2 += 1
                        k -= 1
                        aks[1] -= 1
                        aks[0] = chr(k)
            else: 
              if aks[0]!="G":
                if thesh2>0:
                    a = k+thesh2
                else:
                    a = k-thesh2
                if aks[1]+thesh2>7:
                  while aks[1]<7 and aks[0]!="G":
                    aks[1] += 1
                    k += 1
                    aks[0] = chr(k)
                elif aks[1]+thesh2<0:
                  while aks[1]>1 and aks[0]!="G":
                    aks[1] -= 1
                    b = aks[1]-1
                    k += 1
                    aks[0] = chr(k)
                else: 
                  while thesh2>0 and aks[0]!="G" and aks[1]<7:
                        thesh2 -= 1
                        k += 1
                        aks[1] += 1
                        aks[0] = chr(k)
                     
                  while thesh2<0 and aks[0]!="G" and aks[1]>1:
                        thesh2 += 1
                        k += 1
                        aks[1] -= 1
                        aks[0] = chr(k)
            if aks[1]==pyr[1] and aks[0]==pyr[0]:
                         done = True
                         paikt2 += 1
print("Τα αποτελέσματα των 100 γύρων στην σκακιέρα 7*7 είναι: Παίκτης1(Λευκός Πύργος): ",paikt1,",  Παίκτης2(Μαύρος Αξιωματικός): ",paikt2)
print(" ")

# _A__B__C___D___E__F__G__H_    Σκακιέρα 7*8  
#|__|__|__|___|___|__|__|___|7
#|__|__|__|___|___|__|__|___|6
#|__|__|__|___|___|__|__|___|5
#|__|__|__|___|___|__|__|___|4
#|__|__|__|___|___|__|__|___|3
#|__|__|__|___|___|__|__|___|2
#|__|__|__|___|___|__|__|___|1


paikt1 = 0 #λευκός πύργος
paikt2 = 0 # μαύρος αξιωματικός 
i = 0
arxthesh1 = ["A","B","C","D","E","F","G","H"] #λίστα που χρησιμοποιείται για την τοποθέτηση των πιονιών στις αρχικές τους θέσεις 
arxthesh2 = [1,2,3,4,5,6,7] #λίστα που χρησιμοποιείται για την τοποθέτηση των πιονιών στις αρχικές τους θέσεις
bhm = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
bhmaks = ["aristera","deksia"]
bhmpyr=["katheta","orizontia"]
import random
while i<100:
    i += 1
    pyr = [" ",0]
    aks = [" ",0]
    pyr[0] = random.choice(arxthesh1)
    pyr[1] = random.choice(arxthesh2)
    aks[0] = random.choice(arxthesh1)
    aks[1] = random.choice(arxthesh2)
    done = False
    seira = 1 # 1=παίζει ο άσπρος, 2= παίζει ο μαύρος(Βάζω 1 γιατί τα άσπρα πάντα παίζουν πρώτασ)
    while done == False:
        if seira==1:
             seira = 2
             thesh1 = random.choice(bhmpyr)
             thesh2 = random.choice(bhm)
             if thesh1=="katheta":
                 if pyr[1]+thesh2>7:
                     pyr[1] = 7
                 elif pyr[1]+thesh2<=0:
                     pyr[1] = 1
                 else :
                     pyr[1] += thesh2
             else :
                 k = ord(pyr[0])
                 if k+thesh2>72:
                     pyr[0] = "H"
                 elif k+thesh2<=64:
                     pyr[0] = "A"
                 else:
                     k += thesh2
                     pyr[0] = chr(k)
             if aks[1]==pyr[1] and aks[0]==pyr[0]:
                         done = True
                         paikt1 += 1
        else:
            seira = 1
            thesh1 = random.choice(bhmaks)
            thesh2 = random.choice(bhm)
            k = ord(aks[0])
            if thesh1=="aristera": 
              if aks[0]!="A":
                if thesh2>0:
                    a = k-thesh2 #a=βοηθητική μεταβλητή για να γίνει σωστά η προσθαφαίρεση είτε είναι θετικός είτε αρνητικός 
                else:
                    a = k+thesh2
                if aks[1]+thesh2>7:
                  while aks[1]<7 and aks[0]!="A":
                    aks[1] += 1
                    k -= 1
                    aks[0] = chr(k)   
                elif aks[1]+thesh2<0:
                  while aks[1]>1 and aks[0]!="A":
                    aks[1] -= 1
                    k -= 1
                    aks[0] = chr(k)
                else:
                  while thesh2>0 and aks[0]!="A" and aks[1]<7:
                        thesh2 -= 1
                        k -= 1
                        aks[1] += 1
                        aks[0] = chr(k)
                  while thesh2<0 and aks[0]!="A" and aks[1]>1:
                        thesh2 += 1
                        k -= 1
                        aks[1] -= 1
                        aks[0] = chr(k)
            else: 
              if aks[0]!="H":
                if thesh2>0:
                    a = k+thesh2
                else:
                    a = k-thesh2
                if aks[1]+thesh2>7:
                  while aks[1]<7 and aks[0]!="H":
                    aks[1] += 1
                    k += 1
                    aks[0] = chr(k)
                elif aks[1]+thesh2<0:
                  while aks[1]>1 and aks[0]!="H":
                    aks[1] -= 1
                    b = aks[1]-1
                    k += 1
                    aks[0] = chr(k)
                else: 
                  while thesh2>0 and aks[0]!="H" and aks[1]<7:
                        thesh2 -= 1
                        k += 1
                        aks[1] += 1
                        aks[0] = chr(k)
                     
                  while thesh2<0 and aks[0]!="H" and aks[1]>1:
                        thesh2 += 1
                        k += 1
                        aks[1] -= 1
                        aks[0] = chr(k)
            if aks[1]==pyr[1] and aks[0]==pyr[0]:
                         done = True
                         paikt2 += 1
print("Τα αποτελέσματα των 100 γύρων στην σκακιέρα 7*8 είναι: Παίκτης1(Λευκός Πύργος): ",paikt1,",  Παίκτης2(Μαύρος Αξιωματικός): ",paikt2)