import primepowerFactors
import numpy as np
import qutip as qt

def matFF2ComClass(As):
    '''Accepts a list of numpy arrays or an nxmxm numpy array and returns a set of mubs.'''
    '''Notes for improvement: this code assumes you have a complete set of As. In the paper it 
    states its possible to genereate len(As)+1 MUBS even if Len(As)!=d. It may make sense to 
    reqrite this to accept two distinct arguments ds,As and adjust accoringly.'''
    d=len(As)
    assert len(primepowerFactors(d))==1 , "d is not a Prime Power"
    d,p,k=primepowerFactors(d,returnbases=True)[0]
    assert As[0].shape[0]==As[0].shape[1]==k, "Matrices must be mxm"
    omega=np.exp(2*np.pi*1j/d)
    X=sum([qt.basis(p,(m+1)%p)*qt.basis(p,m).dag() for m in range(p)])
    Z=sum([omega**m*qt.basis(p,m)*qt.basis(p,m).dag() for m in range(p)])
    comclasses=[]
    comclasses+=[[qt.tensor([X**As[0][i,j]*Z**As[1][i,j] for j in range(k)]) for i in range(k)]]
    comclasses+=[[qt.tensor([X**As[1][i,j]*Z**As[m][i,j] for j in range(k)]) for i in range(k)]+[qt.tensor([X**(As[1].sum(0)%p)[j]*Z**(As[m].sum(0)%p)[j] for j in range(k)])]for m in range(d)]
    return comclasses