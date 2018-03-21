# PyMassDNS - Python Wrapper for MassDNS

## About

I often use this tool called [MassDNS](https://github.com/blechschmidt/massdns) which is a high-performance DNS stub resolver. I decided to create this python wrapper to ease the process and for the programmatic challenge.

## Author

[Daniel Abeles](https://twitter.com/Daniel_Abeles).

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
from massdns import MassDNS

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

Since the original massdns tool support many features, I did my best to fit the most and even more. Currently PyMassDNS supports:

*  [Crt.sh](https://crt.sh/) subdomain grabber
*  Worlist based subdomain brute forcer

## TODO

*  Add the rest of the flags of `massdns`

## Credits

[MassDNS](https://github.com/blechschmidt/massdns)
