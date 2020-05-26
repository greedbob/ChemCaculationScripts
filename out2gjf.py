import os, sys


def main(argv):
    if argv:
        for file_name in argv:
            cover(file_name)
    else:
        files = os.listdir('./')
        for file_name in files:
            if file_name[-4:] == '.out':
                cover(file_name)


def cover(file_name):
    periodic_table = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
                      11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}
    new_file_name = file_name[:-4] + '-opted.gjf'
    data = []
    with open(file_name, encoding='utf-8') as file:
        flag = -1
        for line in file:
            if 'Stationary point found' in line:
                flag += 1
            if flag == 0 and 'Input orientation' in line:
                flag += 1
            if flag > 0:
                flag += 1
            if flag > 6:
                if '---' in line:
                    break
                temp = line.split()[1:]
                temp[0] = periodic_table[int(temp[0])]
                data.append(temp)
    with open(new_file_name, 'w') as new_file:
        new_file.write('0 1\n')
        print(new_file_name + '\n0 1')
        for line in data:
            text = ''
            for item in line:
                text += item + '\t'
            print(text.strip())
            new_file.write(text.strip() + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
