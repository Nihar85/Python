Empdetails={}
print(Empdetails)

i=1
while (i<=15):
    Empdetails[i] = {"Name":"User"+str(i),
                       "place":"Place"+str(i)}
    i+=1
print(Empdetails[3])
file=open("mydict.txt","w")
file.write(str(Empdetails))
file.close()

