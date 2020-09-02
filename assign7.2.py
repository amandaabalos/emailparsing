fname = input("Enter file name: ")
fh=open(fname)
count=0
add=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence: ") :
        continue
    #print(line)
    atpos=line.find('0')
    #print(atpos)
    #spos=line.find(' ', atpos)
    #print(spos)
    value=line[atpos:]
    fvalue=float(value)
    #print(value)
    add=add+fvalue
    count=count+1
print ('Average spam confidence:', add/count)
