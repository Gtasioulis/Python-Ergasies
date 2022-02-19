# __________________        Άσκηση 2 p21162
#| t1  |   t2 |   t3|   
#|_____|______|_____| 
#| t4  |   t5 |   t6|
#|_____|______|_____|
#| t7  |   t8 |   t9|
#|_____|______|_____|  

tetragona=["t1","t2","t3","t4","t5","t6","t6","t7","t8","t9"]
kapakia = [1,2,3] #small=1 medium=2 large=3
i = 0
sumbhm=0
import random
while i < 100:
     i += 1
     done = False 
     t1=0 # Αν: t1=0 τότε t1=άδειο, t1=1 έχει μέσα small καπάκι,t1=2 έχει μέσα medium καπάκι,t1=3 έχει μέσα large καπάκι.Ομοία για όλα τα tx 
     t2=0
     t3=0
     t4=0
     t5=0
     t6=0
     t7=0
     t8=0
     t9=0
     bhm=0
     while done== False :
        epkap = random.choice(kapakia) 
        eptet = random.choice(tetragona)
        if eptet=="t1" :
            if epkap>t1 :
                if (epkap>=t4 and epkap>t7) or (epkap<=t4 and epkap<t7) or (t4==0 or t7==0 or epkap==t4==t7): 
                    if (epkap>=t2 and epkap>t3) or (epkap<=t2 and epkap<t3) or (t2==0 or t3==0 or epkap==t3==t2):
                        if (epkap>=t5 and epkap>t9) or (epkap<=t5 and epkap<t9) or (t5==0 or t9==0 or epkap==t5==t9):
                            bhm +=1
                            t1 = epkap
        elif eptet=="t3":
            if epkap>t3 :
              if (epkap>=t2 and epkap>t1) or (epkap<=t2 and epkap<t1) or (t2==0 or t1==0 or epkap==t2==t1):
                  if (epkap>=t5 and epkap>t7) or (epkap<=t5 and epkap<t7) or (t5==0 or t7==0 or epkap==t5==t7):
                      if (epkap>=t6 and epkap>t9) or (epkap<=t6 and epkap<t9) or (t6==0 or t9==0 or epkap==t6==t9):
                        bhm += 1 
                        t3 = epkap 
        elif eptet=="t7":
            if epkap>t7 :
              if (epkap>=t4 and epkap>t1) or (epkap<=t4 and epkap<t1) or (t4==0 or t1==0 or epkap==t4==t1) :
                  if (epkap>=t5 and epkap>t3) or (epkap<=t5 and epkap<t3) or (t5==0 or t3==0 or epkap==t5==t3):
                      if (epkap>=t8 and epkap>t9) or (epkap<=t8 and epkap<t9) or (t8==0 or t9==0 or epkap==t8==t9): 
                        bhm += 1 
                        t7= epkap
        elif eptet=="t9" :
            if epkap>t9 :                                                                                                                                                                   
             if (epkap>=t6 and epkap>t3) or (epkap<=t6 and epkap<t3) or (t6==0 or t3==0 or epkap==t6==t3):
                 if (epkap>=t5 and epkap>t1) or (epkap<=t5 and epkap<t1) or (t5==0 or t1==0 or epkap==t5==t1):
                     if (epkap>=t8 and epkap>t7) or (epkap<=t8 and epkap<t7) or (t8==0 or t7==0 or epkap==t8==t7):
                        bhm += 1
                        t9 = epkap
        elif eptet=="t2" :
            if epkap>t2 :
                if (t1<=epkap and (t3>=epkap or t3==0)) or ((t1 >= epkap or t1==0) and t3<=epkap) or (t1==t3==0):
                    if (epkap>=t5 and epkap>t8) or (epkap<=t5 and epkap<t8) or (t5==0 or t8==0 or epkap==t5==t8):
                        bhm += 1 
                        t2 = epkap 
        elif eptet=="t4":
            if epkap>t4:
                if (t1<=epkap and (t7>=epkap or t7==0)) or (t1 >= epkap and t7<=epkap) or (t1==t7==0):
                    if (epkap>=t5 and epkap>t6) or (epkap<=t5 and epkap<t6) or (t5==0 or t6==0 or epkap==t5==t6):
                        bhm += 1
                        t4 = epkap 
        elif eptet=="t6":
            if epkap>t6:
                if (t3<=epkap and (t9>=epkap or t9==0)) or ((t3==0 or t3 >= epkap) and t9<=epkap) or (t3==t9==0):
                    if (epkap>=t5 and epkap>t4) or (epkap<=t5 and epkap<t4) or (t5==0 or t4==0 or epkap==t5==t4):
                        bhm += 1
                        t6 = epkap 
        elif eptet == "t8":
            if epkap>t8:
                if (t7<=epkap and (t9>=epkap or t9==0)) or ((t7==0 or t7 >= epkap) and t9<=epkap) or (t7==t9==0):
                    if (epkap>=t5 and epkap>t2) or (epkap<=t5 and epkap<t2) or (t5==0 or t2==0 or epkap==t5==t2):
                        bhm += 1
                        t8 = epkap 
        else: 
            if epkap>t5:
                if (t4<=epkap and (t6>=epkap or t6==0)) or ((t4==0 or t4 >= epkap) and t6<=epkap) or (t4==t6==0):
                    if (t2<=epkap and (t8>=epkap or t8==0)) or ((t2==0 or t2 >= epkap) and t8<=epkap) or (t2==t8==0):
                            if (t1<=epkap and (t9>=epkap or t9==0)) or ((t1==0 or t1 >= epkap) and t9<=epkap) or (t1==t9==0):
                                if (t3<=epkap and (t7>=epkap or t7==0)) or ((t3==0 or t3 >= epkap) and t7<=epkap) or (t3==t7==0):
                                    bhm += 1
                                    t5 = epkap 
        if (t1!=0 and t2!=0 and t3!=0) or (t4!=0 and t5!=0 and t6!=0) or (t7!=0 and t8!=0 and t9!=0) or (t1!=0 and t4!=0 and t7!=0 ) or (t2!=0 and t5!=0 and t8!=0) or (t3!=0 and t6!=0 and t9!=0 ) or (t3!=0 and t5!=0 and t7!=0 ) or (t1!=0 and t5!=0 and t9!=0) :
            done = True
     sumbhm += bhm 
mobhm = sumbhm/100
print("Ο μέσος όρος των βημάτων για να λήξει το παιχνίδι είναι:",mobhm)