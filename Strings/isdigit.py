str="my transaction id is 23567"
arr=str.split(" ")
for word in arr:
    if(word.isdigit()):
        print(word)
        break

