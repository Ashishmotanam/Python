s = input(" enter a sentence : ") # creating input for string
print (s)
di = {} # creating empty dictionary
sp = s.split() # splitting each word in dictionary
sp.sort() # sorting the words which are splitted before
#print(sp)
c = 1
#print (sp)
for i in sp: # for loop for getting access to each word in sp
   # print(i)

   if i in di:
        di[i] += c # counting the value if i is repeated in dictionary
   else:
       di[i] = 1   # giving default value of 1 if there is only one word in the string. If there is more than one it will be incremented in if when word appers in string

print (di)





