from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
   name='tagtog2df',
   version='0.1.0',
   author='An Awesome Coder',
   author_email='aac@example.com',
   packages=['tagtog2df'],
   url='http://pypi.python.org/pypi/tagtog2df/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   install_requires= required
)