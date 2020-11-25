import os


key_info = {'b2lypd3': '#p B2PLYPD3/def2TZVP geom=allcheck', 'm052X-vacuum': '#p M052X/6-31G* geom=allcheck',
            'm052x-slv': '#p M052X/6-31G* scrf(SMD,solvent=thf) geom=allcheck'}
files = os.listdir('./')
for file in files:
    if file[-9:] != 'opted.gjf':  # match filename end with 'opted.gjf' only.
        continue
    sys_info, crd_info = [], []
    with open(file) as f:
        for line in f:
            if line[0] == '%':
                sys_info.append(line)
            elif line[0] != '#':
                crd_info.append(line)
        print('Success read file: {}'.format(file))
    for key, value in key_info.items():
        with open(file[:-4] + '-' + key + '.gjf', 'w') as f:
            for line in sys_info:
                f.write(line)
            f.write(value + '\n')
            for line in crd_info:
                f.write(line)
        print('Success write file: {}-{}.gjf.'.format(file[:-4], key))
