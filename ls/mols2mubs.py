def mols2mubs(mols):
    from math import pi
    import qutip as qt
    import numpy as np
    #The input of the function is a set of mutually orthogonal ltin squares formatted as a list of numpy arrays.
    s=mols[0].shape[0]
    d=s**2
    mubs=np.zeros([s+1,d],dtype=object)
    j=0
    molsplus=list(mols)
    molsplus.append(np.resize(np.repeat([np.linspace(1,s,s)],s,0),[s,s]))
    molsplus.append(np.resize(np.repeat([np.linspace(1,s,s)],s,1),[s,s]))
    omega=np.exp((2j*pi)/s)
    for mol in molsplus:
        k=0
        for n in range(1,s+1):
            basisvecs=[]
            alpha=[omega**l for l in range(s)]
            for row in range(s):
                for col in range(s):
                    if mol[row,col]==n:
                        basisvecs.append(qt.tensor(qt.basis(s,row),qt.basis(s,col)))
            for i in range(s):
                alphas=[alpha[i]**m for m in range(s)]
                mubs[j,i+s*k]=sum([alphas[p]*basisvecs[p] for p in range(s)])
            k+=1
        j+=1
    return mubs