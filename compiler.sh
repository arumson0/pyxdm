#!/bin/bash

# Build the fortran kernels.
cd Kernels
  chmod +x build_kernels.sh
  ./build_kernels.sh
cd ..

# Add the driver to the PATH
dir=$(pwd)
chmod +x $dir/driver.py
ln -s $dir/driver.py ./bin/pyxdm

# Remember to add the bin to the path :)
