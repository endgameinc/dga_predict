# Original: https://github.com/baderj/domain_generation_algorithms/blob/master/kraken/v2/dga_v2.py
import random
import time


def rand(r):
    t = (1103515245 * r + 12435) & 0xFFFFFFFF
    return t


def crop(r):
    return (r // 256) % 32768


def generate_domain(index, date, seed_set, temp_file=True, tld_set_nr=1):
    tld_sets = {1: ["com", "net", "tv", "cc"],
                2: ["dyndns.org", "yi.org", "dynserv.com", "mooo.com"],
                3: None}

    seeds = {'a': {'ex': 24938314, 'nex': 24938315},
             'b': {'ex': 1600000, 'nex': 1600001}}
    tlds = tld_sets[tld_set_nr]

    domain_nr = int(index/2)
    if temp_file:
        r = 3*domain_nr + seeds[seed_set]['ex']
    else:
        r = 3*domain_nr + seeds[seed_set]['nex']

    discards = (int(time.mktime(date.timetuple())) - 1207000000) // 604800 + 2
    if domain_nr % 9 < 8:
        if domain_nr % 9 >= 6:
            discards -= 1
        for _ in range(discards):
            r = crop(rand(r))

    rands = 3*[0]
    for i in range(3):
        r = rand(r)
        rands[i] = crop(r)
    domain_length = (rands[0]*rands[1] + rands[2]) % 6 + 7
    domain = ""
    for i in range(domain_length):
        r = rand(r)
        ch = crop(r) % 26 + ord('a')
        domain += chr(ch)

    if tlds:
        domain += "." + tlds[domain_nr % 4]
    return domain


def generate_domains(num_domains, date, seed, tld_set):
    domains = []
    for i in range(num_domains):
        domains.append(generate_domain(i*2, date, seed, random.sample(range(2), 1)[0], tld_set))

    return domains

# import kraken_v2
# from datetime import datetime
# kraken_v2.generate_domains(10, datetime(2016, 1, 1), 'a', 1)
