def isdiag(matrix):
    from numpy import allclose,eye
    '''This function accepts an nxn numpy array and returns True if it is diagonal.'''
    n = matrix.shape[0]
    assert matrix.shape[1] == n, "Matrix must be square to be diagonal."
    return allclose(matrix*eye(n),matrix)