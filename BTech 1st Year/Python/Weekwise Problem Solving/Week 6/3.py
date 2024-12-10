vowels="AEIOUaeiou"
space=" "
count_v = 0
count_c = 0
sentence="My name is Manjesh"

for i in sentence:
    if i == space:
        continue
    elif i in vowels:
        count_v +=1
    else:
        count_c += 1
            
print("Number of Vowels is = ", count_v)
print("Number of consonants is = ", count_c)

biggest = ""

sen = sentence.split()
for  i in sen:
    if len(biggest) < len(i):
        biggest = i
        
print("The largest term is : ", biggest)
str = ""
n = 0

reverse= list()
for i in range(len(sen)-1,-1,-1):
    reverse.append(sen[i])
    str = str + reverse[n] + " "
    n+=1
    
    
print("The reverse of the sentence is ",str)