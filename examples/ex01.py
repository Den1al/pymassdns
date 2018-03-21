from argparse import ArgumentParser, FileType
from pathlib import Path

from massdns import MassDNS

root_dir = Path('/root/recon/massdns/')

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("domain", help="the domain to brute force")
    parser.add_argument("-n", "--names", help="sub domain names list",
        default=root_dir / 'lists' / 'names_small.txt', type=Path)
    parser.add_argument("-r", "--resolvers", help="the resolvers list",
        default=root_dir / 'lists' / 'resolvers.txt', type=Path)
    parser.add_argument("-q", "--quiet", help="whether to print to output to console", action="store_true")
    parser.add_argument("-c", "--cert", help="whether to fetch cert.sh subdomains as well", action="store_true")

    return parser.parse_args()


def main():
    args = parse_args()
    m = MassDNS(root_dir)

    results = m.scan(
        domain=args.domain, 
        names_path=args.names, 
        resolvers_path=args.resolvers, 
        cert_sh=args.cert
    )

    if not args.quiet:
        for result in results:
            print(result)
    

if __name__ == '__main__':
    main()