# http://resources.infosecinstitute.com/domain-generation-algorithm-dga/
# cryptolocker
from datetime import datetime, timedelta


def generate_domain(year, month, day, length=32, tld=''):
    """ Generates a domain by considering the current date. """
    domain = ""

    for i in range(length):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)

    domain += tld

    return domain


def generate_domains(num_domains, seed_num=100, length=32):
    """ Generates a list of domains based on a seed integer. """
    domains = []
    start_date = datetime(2016, 1, 1) + timedelta(days=seed_num)
    for i in range(num_domains):
            new_date = start_date + timedelta(days=i*2+1)
            domains.append(generate_domain(new_date.year, new_date.month, new_date.day, length))
    return domains

# import cryptolocker
# cryptolocker.generate_domains(10, 1)
