
import numpy as np
from Data.atom_info import atom

def cpair(alpha_scl, m1, m2, m3, symbol, l, inputFile):
    c6   = np.zeros((l,l))
    c8   = np.zeros((l,l))
    c10  = np.zeros((l,l))
    rc   = np.zeros((l,l))
    zinv = np.zeros((l,l))

    for i in range(l):
        for j in range(l):
            c6[i][j]   = alpha_scl[i]*alpha_scl[j]*m1[i]*m1[j] / (alpha_scl[i]*m1[j] + alpha_scl[j]*m1[i])
            c8[i][j]   = 1.5 * (alpha_scl[i]*alpha_scl[j]*(m1[i]*m2[j] + m1[j]*m2[i]) / (alpha_scl[i]*m1[j] + alpha_scl[j]*m1[i]))
            c10[i][j]  = 2*(alpha_scl[i]*alpha_scl[j]*(m1[i]*m3[j]+m3[i]*m1[j])/(alpha_scl[i]*m1[j]+alpha_scl[j]*m1[i])) + (21/5)*(alpha_scl[i]*alpha_scl[j]*m2[i]*m2[j] / (alpha_scl[i]*m1[j] + alpha_scl[j]*m1[i]))

            rc[i][j]   = (1/3) * ((c8[i][j]/c6[i][j])**0.5 + (c10[i][j]/c6[i][j])**0.25 + (c10[i][j]/c8[i][j])**0.5)
            zinv[i][j] = 1.0 / (float(atom(symbol[j]).z) + float(atom(symbol[i]).z))

    rmax2 = (np.max(c6)/1.0E-12)**(1/3)
    return c6, c8, c10, rc, zinv, rmax2
