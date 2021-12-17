from data.Ch115.lib.interface import *

def arch_Exists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True

def create_Archive(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print("\033[1;31mThere was an error creating the file!\033[m")
    else:
        print(f'Archive {name} successfully done!')

    
def read_Arch(name):
    try:
        a = open(name,'rt')
    except:
        print("\033[1;31mError reading archive!\033[m")
    else:
        head("REGISTERED PEOPLE")
        #o comando .readlines() volta uma lista com os dados por linha
        #print(a.readlines())
        #O comando .read() volta todas as linhas em texto normal
        for l in a:
            data = l.split(';')
            data[1] = data[1].replace("\n", "")
            print(f'{data[0]:<30} {data[1]}')
        print(a.read())
    finally:
        a.close()

    
def new_Register(arch, name="<unknown>", yod=0):
    try:
        a = open(arch, 'at')
    except:
        print("\033[1;31mThere was an error trying to open the archive\033[m")
    else:
        try:
            a.write(f'\n{name};{yod}')
        except:
            print("\033[1;31mThere was an error trying to write the data\033[m")
        else:
            print(f"New register of {name} added!")
            a.close( )
