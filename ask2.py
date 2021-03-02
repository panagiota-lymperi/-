import random
count = 0
def fibonnaci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonnaci(i-2) + fibonnaci(i-1)
i = int(input("Δώσε όρο ακολουθίας Fibonnaci: "))
print(fibonnaci(i))
oros_fibonnaci= fibonnaci(i)
for i in range(19):
    r = random.randint(1,oros_fibonnaci)
    if (r ** oros_fibonnaci) % oros_fibonnaci == r % oros_fibonnaci:
        flag = 1
    else:
        flag = 0
        count = count + 1
if count > 0:
    print ("Ο όρος", oros_fibonnaci , "ΔΕΝ είναι πρώτος.")
else:
    print ("Ο όρος", oros_fibonnaci , "είναι πρώτος.")
