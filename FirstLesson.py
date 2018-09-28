
def sum(m,n):
    for i in range(abs(n)):
        if n < 0:
            m -= 1
        else:
            m += 1
    return m


def divide(m,n):
    result = 0
    negativeResult = m>0 and n<0 or m<0 and n>0
    n = abs(n)
    m = abs(m)
    
    while (m-n >= 0):
        m -= n
        result +=1
    result = -result if negativeResult else result
    return result

import calculator as c

class FooCalculator(self)

def __init__(self):
    pass

def sum(self, m, n):
    return c.sum(m,n)

def divide(self, m, n):
    return c.divide(m,n)



