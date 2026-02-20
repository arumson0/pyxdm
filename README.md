# pyxdm
This is a python tool to compute XDM dispersion energies, given the output of an electronic structure method already containing XDM data (e.g. Quantum ESPRESSO). The use is to run with alternative damping functions and the Axlerod-Teller-Muto C9 dispersion term.

Currently, the implementation is struggling with FHIaims outputs. Not a high priority for the sole dev at this moment. That may change.

# USAGE:
The compiler adds the pyxdm executable to your path. You may want to copy this to your .bashrc (Sorry windows users, you're on your own.)

`pyxdm input.yaml`

The .yaml file follows this template:
```
input_path:
  - ./examples/ca2n_bulk_b86bpbe-xdmbj.scf.out
file_type: qe

functional: b86bpbe
damping: z
output_unit: Ry

run_settings:
  verbose_conv: true
  pairwise: true
  triples: true
  extrapolate_triples: true
  r2tol: 0.99
```
Tags:
`input_path`: path to the electronic structure method output containing the XDM data. Can be a list of multiple files.

`file_type`: specify whether the method is reading a `qe` or `aims` file.

`functional`: determines the damping parameters for XDM. Currently supports B86bPBE, PBE, and revPBE.

`damping`: type of damping function. Options are 'bj' or 'z'

`output_unit`: What unit you'd like the XDM energy to be expressed in. Options are Ha, Ry, eV, kcal/mol, kj/mol.

`run_settings`:

`verbose_conv`: prints the energy convergence over supercells if true.

`pairwise`: compute the pairwise dispersion contribution (C6, C8, C10)

`triples`: compute the ATM dispersion contribution

`extrapolate_triples`: If true, when the changes in energy become log-linear with R^2 = r2tol, extrapolate the converged energy.

`r2tol`: defines the tolerance for the log-linear regression.

# Notes on the log-linear regression method
The total energy for the ATM term can be extrapolated using a log-linear regression. Doing so can dramatically decrease the computational time required to compute the ATM contribution. Seven points with R^2 >= r2tol are required. This feature is experimental, but a small benchmark on nine simple crystalline system (mix of atomic, molecular, and metallic) suggests the following performance trend.
```
ATM DISPSERION ENERGY
R^2    MAE       ME
0.900: 0.003667% -0.003664%
0.950: 0.003667% -0.003664%
0.975: 0.003351% -0.003349%
0.990: 0.002897% -0.002881%
0.995: 0.000323%  0.000043%
0.999: 0.000323%  0.000043%
N = 9```
The very small errors suggest that the method is generally robust. Based on this benchmark, r2tol is reccomended to be between 0.99 and 0.995.
