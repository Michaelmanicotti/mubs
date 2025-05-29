
def gen_matFF(d):
    from itertools import product
    from itertools import combinations
    from copy import copy
    import numpy as np 
    import primepowerFactors

    assert len(primepowerFactors(d))==1, "dimension D must be as prime power"
    d,p,m=primepowerFactors(d,returnbases=True)[0]

    SymFp = []
    # Fp field elements
    Fp = [i for i in range(p)]

    # Fp^m
    Fpm = list(product(Fp,repeat= m))
    # generate symmetric matrices with elements of Fp

    def det_modp(M1):
        # check for zero determinant ,mod p
        d1 = np.linalg.det(M1)
        d1 = np.around(d1) # round for exact integer
        d1 = d1 % p
        return(d1 != 0)

    def check_lin_comb_B(Bs,bs):
        # check linear combination of B's for nonzero Determinant
        mat = np.zeros((m,m),dtype=int)
        for i in range(m):
            mat += bs[i]*Bs[i]
        val = det_modp(mat)
        return(val != 0)

    def confirm(M1,M2):
        # check determinant of diffeerences
        d1 = det_modp(M1-M2)
        return(d1 != 0)

    def compute_As(Bss):
        # compute A's from B's
        AA = []
        for bs in Fpm:
            mat = np.zeros((m,m),dtype=int)
            for i in range(m):
                mat += bs[i]*Bss[i]
            mat = mat % p
            AA += [mat]
        return(AA)

    prods = product(Fp,repeat= (m*(m+1)//2))

    ind_all_upper = np.triu_indices(m)
    ind_upper = np.triu_indices(m,1)
    ind_lower = np.tril_indices(m,-1)

    for prod in prods:
        sf = np.zeros((m,m),dtype=int)
        sf[ind_all_upper] = prod
        sf[ind_lower] = sf.T[ind_lower]

        if det_modp(sf):
            SymFp += [sf]
    # find basis of B's
    combs = combinations(range(len(SymFp)),m)
    for comb in combs:
        
        # selection of symmetric matrices
        Bs = [SymFp[i] for i in comb]
        
        # check linear combinations have nonzero det
        flag = True
        for bs in Fpm[1:]:
            flag = flag and check_lin_comb_B(copy(Bs),bs)
        
        if flag:
            # generate A's
            AA = compute_As(Bs)
    return AA