# ChemCaculationScripts
Useful scripts for chemical caculation, such as Gaussian, orca and Multiwfn.

## Scripts
script | function
:-: | :-:
ev2kal | cover uint of *B-factor field (i.e. ESP)* in vtx.pdb caculated by Multiwfn.

### ev2kal
The unit of *B-factor field (i.e. ESP)* in vtx.pdb caculated by Multiwfn could be eV or kcal/mol. Use this script to unify the unit to kcal/mol.

`python ev2kal.py vtx.pdb vtx-kcal.pdb`