import sys, re


def ev2kcal(matched):
    value = float(matched.group())
    return str(round(value * 23.060386, 3))


def main(argv):
    file_name, save_name = argv[0], argv[1]
    with open(file_name, encoding='utf-8') as file:
        with open(save_name, 'w') as save_file:
            for line in file:
                if line[-2:] == 'eV':
                    print('The unit of B-factor field (i.e. ESP) is {}, covering'.format('eV'))
                elif line[-8:] == 'kcal/mol':
                    print('The unit of B-factor field (i.e. ESP) is {}, no need to cover.'.format('kcal/mol'))
                    break
                if line[:6] == 'HETATM':
                    temp = re.sub(r'[0-9][.][0-9][0-9]\s', ev2kcal, line[-18:])
                    save_file.write(line[:-18] + temp)
                else:
                    save_file.write(line)


if __name__ == '__main__':
    main(sys.argv[1:])
