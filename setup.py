from setuptools import setup

setup(
   name='clickyang',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['clickyang'],  #same as name
   install_requires=['requests'], #external packages as dependencies
)