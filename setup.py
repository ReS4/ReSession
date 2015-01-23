__author__ = 'Reza Safaeiyan'
from setuptools import setup

setup(
    name='ReSession',
    version='0.1',
    description='ReSession is a Redis-based session for Tornado framework.',
    url='http://github.com/storborg/funniest',
    author='Reza Safaeiyan',
    author_email='Reza_S4T4N@Yahoo.com',
    license='MIT',
    packages=['ReSession'],
    zip_safe=False,
    requires=['redis', 'tornado']
)