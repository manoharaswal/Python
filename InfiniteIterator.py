import itertools

for i in itertools.count(1,2):
    if i > 20:
        break
    else:
        print(i, end=" ")
