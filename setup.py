# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='mpdemo',
    version='0.1.1',
    description='Google Analytics Measurement Protocol helper library.',
    license='no',
    author='yukoga',
    author_email='yukoga@gmail.com',
    url='https://github.com/yukoga/mpdemo.git',
    packages=[
        'mpdemo'],
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: unkown',
        'Operating System :: OS Independent',
    ])
