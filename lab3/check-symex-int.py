#!/usr/bin/python

import symex.fuzzy as fuzzy

def f(x):
    if x == 7:
        return 100
    if x*2 == x+1:
        return 70
    if x > 2000:
        return 80
    if x < 500:
        return 33
    if x / 123 == 7:
        return 1234
    return 40

# def f(x):
#     if x<10:
#         return 10
#     if x>20:
#         return 20
#     else:
#         return 0


# def f(x,y):
#     if(x+y==2):
#         return 2
#     if(x==y):
#         return 0
#     if(x<y):
#         return -1
#     if(x>y):
#         return 1

f_results = set()

# def test_f():
#     i=fuzzy.mk_int('i')
#     j=fuzzy.mk_int('j')
#     v=f(i,j)
#     print i,j,'->',v
#     f_results.add(v)

def test_f():
    i = fuzzy.mk_int('i')
    print "test_f is called "
    v = f(i)
    print i, '->', v
    f_results.add(v)

print 'Testing f..'
fuzzy.concolic_test(test_f, maxiter=200, verbose=10)
#f_expected = (0,-1,1,2)
f_expected = (100, 70, 80, 33, 1234, 40)
if all(x in f_results for x in f_expected):
    print "Found all cases for f"
else:
    print "Missing some cases for f:", set(f_expected) - set(f_results)
