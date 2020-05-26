# ChemCaculationScripts
Useful scripts for chemical caculation, such as Gaussian, orca and Multiwfn.

## Scripts
script | function
:-: | :-
ev2kal | cover uint of *B-factor field (i.e. ESP)* in `vtx.pdb` caculated by Multiwfn.
out2gjf | extract and save final converged structure from `.out` file.

### *`ev2kal.py`*
The unit of *B-factor field (i.e. ESP)* in vtx.pdb caculated by Multiwfn could be eV or kcal/mol. Use this script to unify the unit to kcal/mol.

```bash
python ev2kcal.py vtx.pdb vtx-kcal.pdb
```

### *`out2gjf.py`*
A easy way to extract and save final converged structure from `.out` file.

```bash
python out2gjf.py  # handle all the .out files in current path.
python out2gif.py H2O.out  # extract from H2O.out.
```
