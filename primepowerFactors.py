def primepowerFactors(n,returnbases=False):
    from numpy import asarray
    from math import sqrt
    '''This function accepts an integer n and returns its prime factorization.
    If return bases is False, it reurns a list of the prime powers. If return
    bases is Is True it returns a list of tuples: (factor, primebase,integer power).'''
    '''Citation: This code was based off of a prime factor funtion found here: 
    https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/'''
    assert int(n)==n, "n must be an integer to be factored"
    ppfs=[]
    for i in range(2,int(sqrt(n))+1):
        m=1
        r=0
        while n % i==0:
            m = m*i
            n = n // i
            r+=1
        if m>1:
            if returnbases:
                ppfs.append((m,i,r))
            else:
                ppfs.append(m)
    if n > 1:
        if returnbases:
            ppfs.append((n,n,1))
        else:
            ppfs.append(n)
    return asarray(ppfs)