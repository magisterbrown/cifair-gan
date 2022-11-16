import sys

class Boss:
    def __init__(self):
        self.els = dict()

    def add_command(self, key: str, func: callable):
        self.els[key] = func

    def get_command(self, key):
        return self.els[key]()

def get_cifar():
        from commands.get_cifar import GetCifar as comandor
        return comandor

def cif_to_tar():
        from commands.cif_to_tar import CifToTar as comandor
        return comandor
if __name__=='__main__':
    boss = Boss()
    boss.add_command('get_cifar', get_cifar)
    boss.add_command('cif_to_tar', cif_to_tar)
    
    try:
        subcommand = sys.argv[1]

        Comador = boss.get_command(subcommand) 
        task = Comador(sys.argv[2:])
        task.submit()
    except IndexError:
        print('Options: ')
        print(list(boss.els.keys()))  # Display help if no arguments were given.


    



