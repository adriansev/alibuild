#!/usr/bin/env python
""" Package alibuild using setuptools
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os.path
import sys

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['pyyaml', 'requests', 'distro', 'jinja2']
# Old setuptools versions (which pip2 uses) don't support range comparisons
# (like :python_version >= "3.6") in extras_require, so do this ourselves here.
if sys.version_info >= (3, 6):
    install_requires.append('boto3')

setup(
    name='alibuild',

    description='ALICE Build Tool',
    long_description=long_description,

    # The project's main homepage.
    url='https://alisw.github.io/alibuild',

    # Author details
    author='Giulio Eulisse',
    author_email='giulio.eulisse@cern.ch',

    # Choose your license
    license='GPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',   # slc6
        'Programming Language :: Python :: 3.6',   # slc7, slc8, cs8
        'Programming Language :: Python :: 3.8',   # MacOS
        'Programming Language :: Python :: 3.9',   # alma9
        'Programming Language :: Python :: 3.10',
    ],

    # What does your project relate to?
    keywords='HEP ALICE',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['yaml']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # Single-source our package version using setuptools_scm. This makes it
    # PEP440-compliant, and it always references the alibuild commit that
    # aliBuild was built from.
    use_scm_version={'write_to': 'alibuild_helpers/_version.py'},
    setup_requires=[
        # The 6.* series removed support for Python 2.7.
        'setuptools_scm<6.0.0' if sys.version_info < (3, 0) else
        # The 7.* series removed support for Python 3.6.
        'setuptools_scm<7.0.0' if sys.version_info < (3, 7) else
        'setuptools_scm'
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        ':python_version == "2.7"': ['futures'],
        ':python_version == "2.6"': ['futures', 'argparse', 'ordereddict'],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    include_package_data=True,
    package_data={
      'alibuild_helpers': ['build_template.sh'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    scripts = ["aliBuild", "alienv", "aliDoctor", "aliDeps", "pb"]
)
