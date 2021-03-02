words = []
words2 = []
arxeio = open(input('Δώσε αρχείο ASCII: ' ), 'r')
data = arxeio.read().split()
for x in data:
    words.append(x)
count = 0
for k in words:
    if len(k) <= 19:
        if count < 20:
            count = count + len(k)
            words2.append(k)
        elif count == 20 :
            count = 0
            o = ''.join(words2)
            print(o)
            words2.clear()
            count = count + len(k)
        else:
            count = 0
            words2.clear()
            count = count + len(k)
            words2.append(k)
