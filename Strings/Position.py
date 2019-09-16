str = "my voucher number is (12345)"

pos1=str.find("(")+1
pos2=str.find(")")
print(str[pos1:pos2])