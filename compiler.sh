#!/bin/bash

# Build the fortran kernels.
cd Kernels
  chmod +x build_kernels.sh
  ./build_kernels.sh
cd ..

# Add the driver to the PATH
dir=$(pwd)
mkdir $dir/bin
chmod +x $dir/driver.py
ln -s $dir/driver.py $dir/bin/pyxdm

export PATH=$dir/pyxdm/bin/:$PATH
