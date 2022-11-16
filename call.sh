python3 main.py cif_to_tar -i data/cifar10_res/ -o data/tfolds #Create tfolds for it
python3 submodules/pytorch_GAN_zoo_xla/train.py XLAPGAN -c config_cifar10.json -p 60 #Train xla pgan
