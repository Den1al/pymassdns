from pathlib import Path
from subprocess import Popen, PIPE
from itertools import chain

from massdns.utils import convert_to_path, now_in_str, generate_subdomains, get_crt_sh_subdomains
from massdns.subdomain import Subdomain


class MassDNS(object):
    """ Represents the MassDNS tool wrapper class"""

    def __init__(self, massdns_root_dir):
        self.root_dir = convert_to_path(massdns_root_dir)
        self.default_names_path = self.root_dir / 'lists' / 'names_small.txt'
        self.default_resolvers_path = self.root_dir / 'lists' / 'resolvers.txt'
        self.binary_dir = self.root_dir / 'bin' / 'massdns'
        self.results_folder = self.root_dir / 'results'

        self._create_results_folder()

    def _create_results_folder(self):
        if not self.results_folder.exists():
            self.results_folder.mkdir()


    def scan(self, domain: str, cert_sh=False, names_path=None, resolvers_path=None):
        names_path = convert_to_path(names_path or self.default_names_path)
        resolvers_path = convert_to_path(resolvers_path or self.default_resolvers_path)
        output_path = self.results_folder / f'{domain}_{now_in_str()}.txt'

        command = [
            self.binary_dir,
            '-s', '20000',
            '-r', resolvers_path,
            '-t', 'A',
            '-o', 'S',
            '-w', output_path
        ]

        process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        subs = generate_subdomains(names_path, domain)

        if cert_sh:
            subs = chain(subs, get_crt_sh_subdomains(domain))

        process.stdin.write('\n'.join(subs).encode())

        _ = process.communicate()
        output_data = []

        with output_path.open('r') as f:
            return [Subdomain.from_string(line.strip()) for line in f]
    