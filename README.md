# PyMassDNS - Python Wrapper for MassDNS

## About

I often use this tool called [MassDNS](https://github.com/blechschmidt/massdns) which is a high-performance DNS stub resolver. I decided to create this python wrapper to ease the process and for the programmatic challenge.

## Install

First, follow the installation guide of MassDNS.
Then, if building from source:

```bash
git clone https://github.com/Den1al/pymassdns
cd pymassdns
python setup.py build
python setup.py install
```

Or, just get it from PyPI:

```
pip install pymassdns
```

## Usage

```python
from pymassdns.massdns import MassDNS

# get the massdns root directory

m = MassDNS('/root/recon/massdns/')

results = m.scan('example.com', cert_sh=True)

for result in results:
    print(result)

"""
>>> <Subdomain domain="1001juegos.example.com.", type="A", ip="142.54.173.92"> ...
"""
```

## Features

I added as a flag, to nativly get subdomains from `cert.sh`.

## Credits

[MassDNS](https://github.com/blechschmidt/massdns)
