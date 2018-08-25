# Original: https://github.com/baderj/domain_generation_algorithms/blob/master/corebot/dga.py
from datetime import datetime

def init_rand_and_chars(year, month, day, nr_b, r):
    r = (r + year + ((nr_b << 16) + (month << 8) | day)) & 0xFFFFFFFF
    charset = [chr(x) for x in range(ord('a'), ord('z'))] +\
            [chr(x) for x in range(ord('0'), ord('9'))]
            
    return charset, r

def generate_domain(charset, r, tld=''):
    len_l = 0xC
    len_u = 0x18
    r = (1664525*r + 1013904223) & 0xFFFFFFFF
    domain_len = len_l + r % (len_u - len_l)
    domain = ""
    for i in range(domain_len, 0, -1):
        r = ((1664525 * r) + 1013904223) & 0xFFFFFFFF
        domain += charset[r % len(charset)] 
    domain += tld

    return r, domain

def generate_domains(nr_domains, seed='1DBA8930', d=None, nr_b=1):
    d = d if d else datetime.now()

    charset, r = init_rand_and_chars(d.year, d.month, d.day, 1, 
                                     int(seed, 16)) 

    ret = []
    for _ in range(nr_domains):
        r, d = generate_domain(charset, r)

        ret.append(d)

    return ret

#import corebot
#corebot.generate_domains("1DBA8930", 100000)
