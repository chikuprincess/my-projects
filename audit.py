file=open(r"/home/priya/Desktop/bmc/audit.log","r")
cnt=0
c=file.readlines()
l=[]
for i in c:
    cnt+=1
    h=i.strip().split(" ")
    l.append(h)
log_number=[]
date_time=[]
desc=[]

for i in l:
    log_number.append(i[0])
    date_time.append(i[2])
    desc.append(''.join(str(elem) for elem in i[-5:-2]))
lp=[]

for i in range (cnt):
    print(log_number[i],"\t",date_time[i],"\t",desc[i])
    if not desc[i] in lp:
        lp.append([log_number[i],date_time[i],desc[i]])

