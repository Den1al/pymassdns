import os
from setuptools import setup

from massdns import __version__
from massdns import __author__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pymassdns",
    version = __version__,
    author = __author__,
    author_email = "abeles22@gmail.com",
    description = "This is a python3 wrapper to MassDNS tool",
    license = "BSD",
    keywords = "massdns, bruteforce, dns, scanner",
    url='https://github.com/Den1al/pymassdns',
    packages=['massdns'],
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
    ],
    install_requires=[
          'requests',
      ],
)
