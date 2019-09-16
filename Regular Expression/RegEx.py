import re

data = "AB65BC7DC789"
moddata=re.sub("[A-Za-z]","@",data)
modresult=re.split("@",moddata)

temp=0
for x in modresult:
    if x.isdigit():
        temp=temp+int(x)

print(temp)



