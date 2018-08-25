# Original: https://github.com/baderj/domain_generation_algorithms/blob/master/dircrypt/dga.py
import argparse

class RandInt:

    def __init__(self, seed): 
        self.seed = seed

    def rand_int_modulus(self, modulus):
        ix = self.seed                
        ix = 16807*(ix % 127773) - 2836*(ix / 127773) & 0xFFFFFFFF        
        self.seed = ix
        return ix % modulus 

def generate_domains(nr, seed="1DBA8930", tld=''):
    r = RandInt(int(seed, 16))

    ret = []

    for i in range(nr):
        domain_len = r.rand_int_modulus(12+1) + 8
        domain = ""
        for i in range(domain_len):
            char = chr(ord('a') + r.rand_int_modulus(25+1))
            domain += char
        domain += tld
        
        ret.append(domain)

    return ret

#import dircyrpt
#dircyrpt.generate_domains(10000, "1DBA8930")
