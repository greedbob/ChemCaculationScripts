# [ChemCaculationScripts](https://github.com/greedbob/ChemCaculationScripts)
Useful scripts for chemical caculation, such as Gaussian, orca and Multiwfn.


## Scripts
script | function
:-: | :-
smd-file-generator | generate file to caculate Gibbs free energy with smd (Solvation Model Based on Density)
ev2kal | cover uint of *B-factor field (i.e. ESP)* in `vtx.pdb` caculated by Multiwfn.
out2gjf | extract and save final converged structure from `.out` file.

### *`smd-file-generator.py`*
Use this script to generate files to caculate the Gibbs free energy with smd.
> Reference: [谈谈隐式溶剂模型下溶解自由能和体系自由能的计算](http://sobereva.com/327)

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
