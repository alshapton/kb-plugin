#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup, find_packages


setup(name='kb-plugin',
      version='0.0.1',
      description='A plugin manager for kb, the minimalist knowledge management system',
      keywords=['kb-plugin','kb'],
      author='alshapton',
      author_email='alshapton@gmail.com',
      url='https://github.com/alshapton/kb-plugin',
      #download_url='https://github.com/gnebbia/kb/archive/v0.1.5.tar.gz',
      license='GPLv3',
      long_description=io.open(
          'README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      platforms='any',
      zip_safe=False,
      classifiers=[ 'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Operating System :: OS Independent',
                   ], 
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=["colored","toml","attr","attrs","arrow"],
      python_requires='>=3.6',
      )
