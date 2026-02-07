import numpy as np

def ctriple(alpha_scl, m1,l):
    # Create C9 array:
    c9   = np.zeros((l,l,l))

    # Populate the array
    for i in range(l):
        for j in range(l):
            for k in range(l):
                mionai = m1[i] / alpha_scl[i]
                mjonaj = m1[j] / alpha_scl[j]
                mkonak = m1[k] / alpha_scl[k]
                c9[i][j][k] = m1[i]*m1[j]*m1[k]*(mionai + mjonaj + mkonak) / ((mionai + mjonaj)*(mionai + mkonak)*(mjonaj+mkonak))
    return c9
