# pyxdm
This is a python tool to compute XDM dispersion energies, given the output of an electronic structure method already containing XDM data (e.g. Quantum ESPRESSO). The use is to run with alternative damping functions and the Axlerod-Teller-Muto C9 dispersion term.

Currently, the implementation is struggling with FHIaims outputs. Not a high priority for the sole dev at this moment. That may change.

# USAGE:
The compiler adds the pyxdm executable to your path. You may want to copy this to your .bashrc (Sorry windows users, you're on your own.)
To run, you will need a .yaml file following this template:
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

```
Tags:
`input_path`: path to the electronic structure method output containing the XDM data. Can be a list of multiple files.\n
`file_type`: specify whether the method is reading a `qe` or `aims` file.\n
`functional`: determines the damping parameters for XDM. Currently supports B86bPBE, PBE, and revPBE.\n
`damping`: type of damping function. Options are 'bj' or 'z'\n
`output_unit`: What unit you'd like the XDM energy to be expressed in. Options are Ha, Ry, eV, kcal/mol, kj/mol.\n
`run_settings`:\n
    `verbose_conv`: prints the energy convergence over supercells if true.\n
    `pairwise`: compute the pairwise dispersion contribution (C6, C8, C10)\n
    `triples`: compute the ATM dispersion contribution\n
    `extrapolate_triples`: Very large performance improvement to be gained with this. If true, when the changes in energy become log-linear with R^2 = 0.99, extrapolate the converged energy. Initial testing suggests that this is a very robust method (errors <0.01%).\n
