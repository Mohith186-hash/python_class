def feed(l):
    return l
l=['1..100','101..200','302..400','401..500']
print(feed(l))

def feed(l):
    yield l
l=['1..100','101..200','302..400','401..500']
load=feed(l)
print(next(load))

def feed(l):
    for i in l:
        yield i
l=['1..100','101..200','302..400','401..500']
load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))

def feed(l):
    for i in l:
        yield i
l=['File 1','File 2','File 3','File 4','File 5']
load=feed(l)
print(next(load))
print(next(load))
print(next(load))
print(next(load))