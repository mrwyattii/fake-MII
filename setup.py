'''
Copyright 2022 The Microsoft DeepSpeed Team
'''

from setuptools import setup, find_packages


install_requires = ["fake_ds", "pytest"]

setup(name="fake_mii",
      version="1.0",
      description='fake MII',
      install_requires=install_requires,
      packages=find_packages(),
      )
