from setuptools import setup, find_packages

cmec_version = 1
packages = find_packages()
scripts = ['python/cmec-driver.py']
entry_points = {}

setup(
    name='cmec-driver',
    version=cmec_version,
    author='CMEC',
    description = 'cmec driver',
    url='https://cmec.llnl.gov/',
    packages=packages,
    scripts=scripts)