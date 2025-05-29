def isls(square):
    rows,colms=square.shape
    if rows!=colms:
        print("Matrix not Suqare")
        return False
    for row in range(rows):
        countedinrow=[]
        for j in range(colms):
            if square[row,j] in countedinrow:
                print("Matrix is not Latin Square.\n", square[row,j]," appears twice in row ",row,"." )
                return False
            else:
                countedinrow.append(square[row,j])
    for colm in range(colms):
        countedincolm=[]
        for i in range(rows):
            if square[i,colm] in countedincolm:
                print("Matrix is not Latin Square.\n", square[i,colm]," appears twice in column ",colm,"." )
                return False
            else:
                countedincolm.append(square[i,colm])
    return True