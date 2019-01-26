time=(input().strip())
retime=""
amorpm=time[-2:]
if (amorpm=="PM"):
    if int(time[0:2])<12:
        retime+=str(12 + int(time[0:2])) + time[2:-2]
    else:
        retime+= str(int(time[0:2])) + time[2:-2]
else:
    if time[0:2]=="12":
        retime+="00"+ time[2:-2]
    else:
        retime+=time[:-2]
print (retime)
