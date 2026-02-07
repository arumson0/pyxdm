import numpy as np

def qe_reader(inputFile):
    # Initialize emptry arrays:
    volscl = np.array([])
    alpha = np.array([])
    m1 = np.array([])
    m2 = np.array([])
    m3 = np.array([])
    index = np.array([])
    symbol = []
    positions = np.array([])
    mtrx = np.array([])

    # Get volume scaling and multipole moments:
    with open(inputFile) as f:
        for line in f:
            if "+ Volumes and moments" in line:
                break
        next(f)
        next(f)
        for line in f:
            line = line.strip()
            if not line:
                break
            line = line.split()
            volscl = np.append(volscl,float(line[1])/float(line[2]))
            m1 = np.append(m1,float(line[3]))
            m2 = np.append(m2,float(line[4]))
            m3 = np.append(m3,float(line[5]))
    
    # Get atomic numbers and polarizabilities:
    with open(inputFile) as f:
        for line in f:
            if "site n." in line:
                break
        for line in f:
            line = line.strip()
            if not line:
                break
            line = line.split()
            index = np.append(index, int(line[0]))
            symbol.append(str(line[1]))
            positions = np.append(positions, np.array([float(line[6]),float(line[7]),float(line[8])]))
        tau = np.reshape(positions, (-1,3))
    # get the a-lattice parameter
    with open(inputFile) as f:
        for line in f:
            if "lattice parameter (alat)  =" in line:
                line = line.split()
                alat = float(line[4])
    # get the lattice vectors in terms of alat 
    with open(inputFile) as f:
        for line in f:
            if "crystal axes:" in line:
                break
        for line in f:
            line = line.strip()
            if not line:
                break
            line = line.split()
            mtrx = np.append(mtrx,np.array([float(line[3]),float(line[4]),float(line[5])]))
        mtrx = alat*np.reshape(mtrx,(3,3))

    return m1,m2,m3, volscl, alpha, symbol, alat, tau, mtrx

def aims_reader(inputFile):
    # Initialize emptry arrays:
    volscl = np.array([])
    alpha = np.array([])
    m1 = np.array([])
    m2 = np.array([])
    m3 = np.array([])
    index = np.array([])
    symbol = []
    positions = np.array([])
    mtrx = np.array([])

    # Get the volume scaling and multipole moments
    with open(inputFile) as f:
        for line in f:
            if "+ Volumes and moments" in line:
                break
        next(f)
        for line in f:
            line = line.strip()
            if "Converging" in line:
                break
            line = line.split()
            volscl = np.append(volscl, float(line[4])/float(line[2]))
            m1 = np.append(m1, float(line[6]))
            m2 = np.append(m2, float(line[7]))
            m3 = np.append(m3, float(line[8]))

    # Get atomic numbers and polarizabilities
    with open(inputFile) as f:
        for line in f:
            if "in the first line of geometry.in ." in line:
                break
        next(f)
        next(f)
        next(f)
        for line in f:
            line = line.strip()
            if not line:
                break
            line = line.split() 
            if "lattice_vector" in line:
                mtrx = np.append(mtrx,np.array([float(line[1]),float(line[2]),float(line[3])]))
            elif "atom_frac" in line:
                positions = np.append(positions, np.array([float(line[1]),float(line[2]),float(line[3])]))
                symbol.append(str(line[4]))

        mtrx = np.reshape(mtrx,(3,3)) * 1.8897259886
        fraccoords = np.reshape(positions, (-1,3))
        alat = np.linalg.norm(mtrx[0,:])
        tau = np.matmul(fraccoords,mtrx) / alat

    return m1,m2,m3, volscl, alpha, symbol, alat, tau, mtrx
