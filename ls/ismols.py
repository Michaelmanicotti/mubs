def ismols(mols):
    import isls
    s=mols[0].shape[0]
    i=0
    for mol in mols:
        if not isls(mol):
            print(i," is not a latin square.")
            return False
        i+=1
    if len(mols)>1:
        combs=[]
        for i in range(s):
            for j in range(s):
                comb=[mol[i][j] for mol in mols]
                if comb in combs:
                    print("Latin Squares are Not Mutually Orthogonal") 
                    return False
                else:  
                    combs.append(comb)
    return True