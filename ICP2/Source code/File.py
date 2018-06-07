file = open("Pfile.txt","r")
for i in file:
    l = len(i)
    file1 = open("Rfile.txt","a")
    file1.write(i[:-1]+","+str(l-1))
file1.close()
