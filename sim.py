
import time
print ("\033c\033[43;30m\nenter simulator\n")
def sims(n):
    totals=0
    rets=[]
    nn=0
    t=True
    while t:
        print(str(totals)+" units")
        totals=totals+n
        if totals>10:
            totals=0
            print("8 units to hood as material")
            print("2 units to hood as energy")
        time.sleep(1)
    
sims(1)