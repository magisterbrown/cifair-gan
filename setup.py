from setuptools import setup, find_packages
import re

try:
    from pip._internal.operations import freeze
except ImportError:
    from pip.operations import freeze

installed_names = map(lambda x:re.match('\w+',x).group(), freeze.freeze())

exceptions = [
        '@ file',
    ]

with open('requirements.txt', 'r') as f:
    deps = f.readlines()

    #Remove packages that have patterns from the exceptios
    for exc in exceptions:
        deps = list(filter(lambda x:not (exc in x), deps))
    
    #Dont install already installed packages
    installed = list(installed_names)
    filteter = lambda x:not (re.match('\w+',x).group() in installed)
    deps = list(filter(filteter, deps))

#Find packages in base dir and search_dirs
search_dirs = [ 'submodules/pytorch_GAN_zoo_xla' ]
package_dirs = dict()
packages = list()
for pdr in search_dirs:
    new_packs = find_packages(where=pdr)
    for npk in new_packs:
        if '.' not in npk:
            package_dirs[npk] = f'{pdr}/{npk}'

    packages += new_packs

packages += find_packages()
setup(name='cifart',
      version='1.0',
      description='',
      author='magisterbrownie',
      author_email='magisterbrownie@gmail.com',
      url='',
      packages=packages,
      package_dir = package_dirs,
      install_requires=deps
     )











