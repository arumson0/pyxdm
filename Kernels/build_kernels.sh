#!/bin/bash
# Compile Fortran kernels into Python extensions

echo "Compiling Fortran kernels..."

# Use gfortran + f2py
python3 -m numpy.f2py -c pairwise_xdm.f90 -m cpair_kernel --f90flags="-O3 -fopenmp" -lgomp
python3 -m numpy.f2py -c c9_loops.f90 -m c9_kernel  --f90flags="-O3 -fopenmp" -lgomp

echo "Done. You should now see cpair_kernel*.so and c9_kernel*.so"
