class Subdomain(object):
    """ Represent a subdomain tuple """
    def __init__(self, domain, typ, ip):
        self.domain = domain
        self.typ = typ
        self.ip = ip

    def __repr__(self):
        return f'<Subdomain domain="{self.domain}", type="{self.typ}", ip="{self.ip}">'

    @staticmethod
    def from_string(some_string):
        parts = some_string.split()
        if len(parts) != 3:
            raise ValueError('The string should have three parts')
        
        return Subdomain(parts[0], parts[1], parts[2])