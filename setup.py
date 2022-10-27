'''
Copyright 2022 The Microsoft DeepSpeed Team
'''

from setuptools import setup, find_packages


def fetch_requirements(path):
    with open(path, 'r') as fd:
        return [r.strip() for r in fd.readlines()]


install_requires = fetch_requirements('requirements/requirements.txt')

setup(name="fake_mii",
      version="1.0",
      description='fake MII',
      install_requires=install_requires,
      packages=find_packages(),
      )
