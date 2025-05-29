def iscomclass(comclass):
    import numpy as np
    '''Function accepts a list of numpy arrays or an nxmxm numpy array.
    It returns True if all the matrices commute and false it they do not.'''
    doescommute=True
    for i in range(len(comclass)): 
        for j in range(i,len(comclass)):
            if not np.all((comclass[i]*comclass[j]-comclass[j]*comclass[i]).full()<1e-15):
                doescommute=False
    return doescommute