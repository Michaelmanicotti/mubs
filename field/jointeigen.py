import numpy as np
import qutip as qt
import iscomclass
import isdiag
import extractblocks

def jointeigen(comclass):
    '''
    Inputs: commclass- a commuting class of matrices, a list of nxn QObj operators
    Returns: jointeigenstates: the states that make up the joint eigenbasis for the commuting class,
    a 1xn numpy array of Qobj state vectors that form a basis
    '''
    n = comclass[0].shape[0]
    for i in range(len(comclass)):
        assert comclass[i].shape[0]==comclass[i].shape[1] == n, "Matrices in commuting class must be square and the same size."
    assert iscomclass(comclass), "Matrices in class must commute."

    P=np.linalg.eig(comclass[0].full())[1]
    Pinv=np.linalg.inv(P)

    assert isdiag(Pinv@comclass[0].full()@P), "Error: Eigenvectors do not diagonalize matrix 0."
    for i in range(1,len(comclass)):
        if isdiag(Pinv@comclass[i].full()@P):
            print('pass')
            pass
        else:
            BinbasisA=P@comclass[i].full()@Pinv
            blocksofB=extractblocks(BinbasisA)#unpack this better
            neweigens=np.zeros((n,n),dtype=np.complex128)
            for j in range(len(blocksofB)):
                neweigens[blocksofB[j][1][0]:blocksofB[j][1][1],blocksofB[j][1][0]:blocksofB[j][1][1]]=np.linalg.eig(blocksofB[j][0])[1]
            P=Pinv@neweigens
            Pinv=np.linalg.inv(P)
            assert isdiag(Pinv@comclass[i].full()@P), "Error: Eigenvectors do not diagonalize matrix "+str(j)
    jointeigenstates=np.zeros(n,dtype=qt.Qobj)
    for i in range(n):
        jointeigenstates[i]=qt.Qobj(P[:,i])
    return jointeigenstates
