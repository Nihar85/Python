import re

def extractpattern_data(sourcestring,pattern):
    return re.findall(pattern,sourcestring)

string='My Pan Number is HJIPM4600E'
ptrn="[A-z]{5}[0-9]{4}[A-z]{1}"


print(extractpattern_data(string,ptrn))