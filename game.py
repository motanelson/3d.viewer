import os
def loads(s):
    f1=open(s,"r")
    r=f1.read()
    f1.close()
    rr=r.split("\n")
    for n in range(len(rr)):
        rrr=rr[n].split("=")
        print(str(n)+":"+rrr[0])
    ss=input("give a option ? ")
    i=int(ss)
    rrr=rr[i].split("=")
    if len(rrr)<2:
        return ""
    else:
        
        return rrr[1]
print("\033c\033[43;30m\n")
print("Welcome brave knight the kingdom needs you")
print("An evil shadow threatens the land What will be your fate")
t=True
s="main.txt"
back=s
while t:
    if s.find(".txt")>-1:
        back=s
        sss=s.split("!")
        xo='explorer.exe "'+ os.getcwd()+"\\" +sss[0].replace(".txt",".mp4")+'"'
        print(xo)
        os.system (xo)
        s=loads(sss[0])
        
    else:
        sss=s.split("!")
        s=loads(sss[0])
        
    if s=="":
        t=False
    else:
        if s.find(".txt")<0:
            sss=s.split("!")
            if len(sss)>1:
                print(sss[1]) 
    