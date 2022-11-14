from setuptools import setup, find_packages

try:
    from pip._internal.operations import freeze
except ImportError:
    from pip.operations import freeze

installed_names = map(lambda x:x.split('=')[0], freeze.freeze())

exceptions = [
        '@ file',
    ]

with open('requirements.txt', 'r') as f:
    deps = f.readlines()

    #Remove packages that have patterns from the exceptios
    for exc in exceptions:
        deps = list(filter(lambda x:not (exc in x), deps))
        installed_names = list(filter(lambda x:not (exc in x), installed_names))

    #Dont install already installed packages
    for installed in installed_names:
        filteter = lambda x:not (installed in x.split('=')[0])
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
print(deps)
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











