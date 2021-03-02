arxeio = open(input('Δώσε αρχείο ASCII: ' ), 'r')
data = arxeio.read().split()
#for x in data:
for x in data[-1:0:-1]:
    for i in x:
        n_c = ord(i)
        k = chr(128 - n_c)
        print(k[-1::-1], end="")
arxeio.close()
