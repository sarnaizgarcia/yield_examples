def infinite():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite()
print(next(gen))
print(next(gen))
print(next(gen))
