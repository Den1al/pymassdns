from pathlib import Path
from datetime import datetime
import requests
import re

_cert_sh_domain_regex = re.compile(r'<td>([\d\w\-\.]*?)<\/td>', re.I)

def convert_to_path(some_path):
    """ Safely converts a string like path, to a pathlib variant """
    if type(some_path) == str:
        return Path(some_path)
    elif type(some_path) == Path:
        return some_path
    else:
        raise ValueError('Can\'t conver to Path')

def generate_subdomains(fname: Path, domain: str):
    """ Reads subdomin prefixes - lazy """

    with fname.open('r') as f:
        for line in f:
            sub_domain = line.strip()
            yield f'{sub_domain}.{domain}'

def now_in_str():
    """ Gets todays date in a string form """
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def get_crt_sh_subdomains(domain: str) -> list:
    """ Extracts subdomains from cert.sh """
    def _find_domain_in_body(html_body: str) -> set:
        domains = set()

        for match in _cert_sh_domain_regex.finditer(html_body):
            domains.add(match[1].lower())

        return domains

    url = f'https://crt.sh/?q=%25{domain}'
    r = requests.get(url)

    return _find_domain_in_body(r.text)