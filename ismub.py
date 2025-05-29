def ismub(mub):
    tollerance=1e-15
    nbases,d=mub.shape
    if not d==mub[0].size==mub[0][0].shape[0]:
        print("Not the right number of vectors to form a basis.")
        return False
    for i in range(nbases):
        for m in range(d):
            if mub[i][m]!= mub[i][m].unit():
                print("Basis ",i," is not an orthonormal basis. \nVector ",m," is not normalized.")
                return False
            for n in range(m+1,d):
                if abs(mub[i][m].overlap(mub[i][n]))>tollerance:
                    print("Basis ",i," is not an orthonormal basis. \nVectors ", m," and ",n," are not orthogonal.",abs(mub[i][m].overlap(mub[i][n])))
                    return False
    for i in range(nbases):
        for j in range(i+1,nbases):
            for m in range(d):
                for n in range(d):
                    if abs(mub[i][m].overlap(mub[j][n]))**2-(1/d)>tollerance:
                        print("Bases are not mutually unbiased. \n Overlap basis",i," vector ",m," basis ",j," vector ",n,"=",abs(mub[i][m].overlap(mub[j][n]))**2)
                        return False         
    return True