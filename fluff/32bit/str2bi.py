val = 'flag.txt'
res = '\n'.join(format(ord(i), 'b') for i in val) 
print("{}".format(res))