# Original: https://github.com/baderj/domain_generation_algorithms/blob/master/pykspa/improved/dga.py
import json
import argparse
from datetime import datetime
import time

import sys
import os

def get_sld(length, seed):
    sld = ""
    modulo = 541 * length + 4
    a = length * length
    for i in range(length):
        index = (a + (seed*((seed % 5) + (seed % 123456) +
            i*((seed & 1) + (seed % 4567))) & 0xFFFFFFFF))  % 26
        a += length;
        a &= 0xFFFFFFFFF
        sld += chr(ord('a') + index)
        seed += (((7837632 * seed * length) & 0xFFFFFFFF) + 82344) % modulo;
    return sld


def generate_domains(nr, date=None, set_nr=2, add_tld=False):
    if not date:
        date = datetime.now()

    fl = os.path.join(os.path.dirname(os.path.realpath(__file__)), "set{}_seeds.json".format(set_nr))
    with open(fl, "r") as r:
        seeds = json.load(r)
    dt = time.mktime(date.timetuple())
    days = 20 if set_nr == 1 else 1
    index = int(dt//(days*3600*24))
    if str(index) not in seeds:
        print("Sorry, {} is out of the time range I know".format(date))
        return
    seed = int(seeds.get(str(index), None), 16)
    original_seed = seed 

    ret = []
    for dga_nr in range(nr):
        # determine next seed
        s = seed % (dga_nr + 1)
        seed += (s + 1)
        
        # second level length
        length = (seed + dga_nr) % 7 + 6  

        # get second level domain
        second_level_domain = get_sld(length, seed)

        # get first level domain
        if add_tld:
            tlds = ['com', 'net', 'org', 'info', 'cc']
            top_level_domain = tlds[(seed & 3)]

            # concatenate and print domain
            domain = second_level_domain + '.' +  top_level_domain
        else:
            domain = second_level_domain
        ret.append(domain)

    return ret


#import pykspa
#import datetime
#pykspa.generate_domains(datetime.datetime.now(), 10000, 2)
#or
#pykspa.generate_domains(datetime.datetime.now(), 10000, 2)

