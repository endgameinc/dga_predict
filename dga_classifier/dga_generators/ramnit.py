# Original: https://github.com/baderj/domain_generation_algorithms/blob/master/ramnit/dga.py
class RandInt:

    def __init__(self, seed): 
        self.seed = seed

    def rand_int_modulus(self, modulus):
        ix = self.seed                
        ix = 16807*(ix % 127773) - 2836*(ix / 127773) & 0xFFFFFFFF        
        self.seed = ix 
        return ix % modulus 

def get_domains(seed, nr, add_tld=False):
    r = RandInt(seed)

    for i in range(nr):
        seed_a = r.seed
        domain_len = r.rand_int_modulus(12) + 8
        seed_b = r.seed
        domain = ""
        for i in range(domain_len):
            char = chr(ord('a') + r.rand_int_modulus(25))
            domain += char

        if add_tld:
            domain += ".com"
            
        m = seed_a*seed_b
        r.seed = (m + m//(2**32)) % 2**32 
        yield domain

def generate_domains(nr, seed, add_tld=False):
    return [x for x in get_domains(seed, nr, add_tld)]

#import ramnit
#domains = ramnit.generate_domains(0x123abc12, 10)