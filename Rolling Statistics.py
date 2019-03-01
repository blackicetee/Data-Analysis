import math
'''Refreshing knowledge about statistic math!'''

l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [0.1,0.2,0.3,0.4]
l3 = [213,23,132,543,-234,-34643]
l4 = [21.,50.,62.,85.,90.]
l5 = [4,7,10,15,18]

def my_count(l):
    count = 0
    for element in l:
        count +=1
    return count

print(my_count([0,1,2,3,4,5]))

def my_sum(l):
    base = 0
    for element in l:
        base += element
    return base

print(my_sum(l1))

def my_mean(l):
    base = 0.0
    count = 0
    for element in l:
        base += element
        count += 1
    return (base / count)

print(my_mean(l4))

def my_min(l):
    m = l[0]
    for e in l:
        if e < m:
            m = e
    return m

print(my_min(l3))

def my_max(l):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

print(my_max(l3))

'''Standard Deviation:
Standard deviation is a measure of spread,
that is -> how spread out is a set of data?
Standard Deviation: LOW
-> The data is closely clustered around the mean(or average).
Standard Deviation: HIGH
-> The data is dispersed(distributed or spread over a wide area)
over a wider range of value.
Standard Deviation is represented
by the small greek letter sigma(looks like a bendet number six).
Standard Deviation allows us to determine,
whether a value is statistical significant or part of expected variation.
e.g. a european person which is 3 m tall will be probably
statistically significant, but a e person which is 1.7 m tall will be
probably part of expected variation
'''

def std_dev(l):
    dev = 0.0
    n = len(l) - 1
    mean = my_mean(l)
    for e in l:
        dev += (e - mean) ** 2
    return math.sqrt((dev / n))

print(std_dev(l4))
