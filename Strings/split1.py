mystr = "india training india hotels india infra india manufacture"
arr = mystr.split(" ")

count=0
for item in arr:
    if(item=='india'):
        count+=1
print(count)