def infinite():
    num = 0
    while True:
        yield num
        num += 1


for i in infinite():
    print(i)
