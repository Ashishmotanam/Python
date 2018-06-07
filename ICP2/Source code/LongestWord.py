from typing import List

a = ["PHP", "Exercise", "Backend","Ashish"]
b =[]
le = len(a)
#print(le)
for i in range(le):
    c=()
    c = (len(a[i]),a[i])
    #print (c)
    b.insert(i,c)
#print(b)

b.sort()
print(b[-1])