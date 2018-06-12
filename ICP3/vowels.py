s = input(" enter a sentence : ") # giving string input
print (s)
v = {'a','e','i','o','u','A','E','I','O','U'} # creating set with all vowels (both upper and lower case)
c =0
for i in s:      # for loop for getting each letter in string
    for j in v:  # for loop for getting access to each letter in set of vowels
        if(i==j):
            c = c+1  # incrementing count if letter in string equals letter in set
print(c)