pattern="*"
temp=""
for r in range(1,6):
    for c in range(1,r+1):
        temp=temp+pattern
    print(temp)
    temp=""