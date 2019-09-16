mystr = "the global id is:1537 the trans code is : 23456 the journal number : 27809"
temp = ""
for i in range (0, len(mystr)):
    if (i+1 != len(mystr)):
        if (mystr[i].isdigit() and mystr[i+1].isspace()):
            temp=temp+mystr[i]+"@"
        else:
            temp = temp+mystr[i]
    else:
        temp = temp + mystr[i]
arr = temp.split("@")

for word in arr:
    print(word.strip().capitalize())



