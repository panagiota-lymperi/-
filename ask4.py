import random
list_word = []
list_word2 = []
list_word3 = []
arxeio = open(input('Δώσε αρχείο ASCII: ' ), 'r')
ded = arxeio.read().split()
for x in ded:
    list_word.append(x)
N=3
list_word2 = [list_word[n:n+N] for n in range(0, len(list_word), N)]
random_index = random.randint(0,len(list_word2)-1)
x = list_word2[random_index]
print(x)
for i in x:
    list_word3.append(i)
i = [1,2]
element = []
for index in i:
    element.append(x[index])
count = 0
while count <= 200 or len(list_word2) > 0:
    random_index = random.randint(0,len(list_word2)-1)
    x2 = list_word2[random_index]
    pos = list_word2.index(x2)
    i2 = [0,1]
    element2 = []
    for index in i2:
        element2.append(x2[index])
    if element == element2 :
        count = count + 1
        list_word2.pop(pos)
        list_word3.append(x2[2])
    else:
        list_word2.pop(pos)
if count == 0:
    print ("Δεν υπάρχουν κοίνες δυάδες.")
else:
    print (list_word3)
