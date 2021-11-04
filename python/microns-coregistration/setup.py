#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, '..', 'version.py')) as f:
    exec(f.read())

def find_config_package(name):
    return f"{name} @ file://localhost/{here}/../{name}#egg={name}"

config_package = find_config_package('microns-coregistration-config')

setup(
    name='microns-coregistration',
    version=__version__,
    description='EM/Functional coregistration for MICrONS',
    author='Stelios Papadopoulos',
    author_email='spapadop@bcm.edu',
    packages=find_packages(exclude=[]),
    install_requires=['numpy', 'scipy', 'tqdm', 'pandas', 'seaborn', 'matplotlib', 'torch', config_package]
)