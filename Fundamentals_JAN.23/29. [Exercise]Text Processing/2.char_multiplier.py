line = input().split()
string1 = list(line[0])
string2 = list(line[1])
charsum = 0

for idx, chr in enumerate(string1):
    try:
        charsum += ord(chr) * ord(string2[idx])
    
    except:
        charsum += ord(chr)
    
    
if len(string2) > len(string1):
    diff = len(string2) - len(string1)
    string2_diff = string2[-diff:]
    for ch in string2_diff:
        charsum += ord(ch)
print(charsum)

