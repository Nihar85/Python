#Step 1
import json

#Step 2
dumpdata={
    "name":"nihar",
    "age":"32",
    "place":"Hyderabad",
    "Location":"Kukatpally"
}
#Step 3
jsondumpdata=json.dumps(dumpdata)
print(type(jsondumpdata))
#Step 4
jsonfile=open(r"Testdata.json","w")
jsonfile.write(jsondumpdata)