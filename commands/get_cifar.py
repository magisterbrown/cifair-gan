from .base_command import BaseCommand
import os
import json

class GetCifar(BaseCommand):
    def __init__(self,inputs):
        self.add_arg('o','out','path to save ds')
        super().__init__(inputs)

        self.path = self.pathify(self.args.out)

    def submit(self):
        os.system(f'gsutil cp gs://monet-cool-gan/cifar10gn.tar {self.path}')
        os.system(f'tar -xf {self.path}cifar10gn.tar -C {self.path}')
        json_pth=f'{self.path}config_cifar10.json'
        #with open(json_pth, "r+") as f:
        #    json_repr = json.load(f)
        #    json_repr['pathDB'] = f'{self.path}cifar10_res/'
        #    f.write(json.dumps(json_repr))



