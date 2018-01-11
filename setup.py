#!/usr/bin/env python
"""Setup script for the project."""

from setuptools import setup

VERSION = '0.0.1'

setup(
    author='Team per la Trasformazione Digitale',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    description='Sphinx extension that retrieves the tag of the last project version on RTD.',
    install_requires=['sphinx'],
    keywords='sphinx project version tag reagthedocs',
    license='BSD-3-clause',
    name='sphinxcontrib-versiontag',
    packages=['sphinxcontrib'],
    package_data={},
    version=VERSION,
    zip_safe=False,
)
