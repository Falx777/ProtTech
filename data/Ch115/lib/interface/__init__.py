def row(size = 40):
    return '='*size


def head(txt):
    print(row())
    print(txt.center(40))
    print(row())


def read_int(nbr):
    read = 0
    while True:
        try:
            num = int(input(nbr))
            read = int(num)
        except KeyboardInterrupt:
            read = 0
        except:
            print("")
            print("\033[1;31mErro: Digitate a valid integer number! \033[m")
        else: 
            break
    return read


def menu(lst):
    head("MAIN MANU")
    c = 0
    for i in lst:
        print(f'\033[1;33m{c + 1}\033[m - \033[1;34m{i}\033[m')
        c += 1
    print(row()) 
    opt = read_int("Your option:")
    return opt
