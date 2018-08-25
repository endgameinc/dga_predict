# Ramdo DGA
# https://www.damballa.com/behind-ramdo-dga-domain-generation-algorithm/


def generate_domain(seed_num, domain_iterator, length=0x10, add_tld=False):

    xor1 = 0
    sh1 = seed_num << 1
    domain_iterator += 1
    step1 = domain_iterator * sh1
    # step1b = domain_iterator * seed_num
    domain_iterator -= 1
    iter_seed = domain_iterator * seed_num
    imul_edx = iter_seed * 0x1a
    xor1 = step1 ^ imul_edx
    domain_length = 0
    dom = ''

    while domain_length < length:
        # xor1_divide = xor1 / 0x1a
        xor1_remainder = xor1 % 0x1a
        xo1_rem_20 = xor1_remainder + 0x20
        xo1_step2 = xo1_rem_20 ^ 0xa1
        dom_byte = 0x41 + (0xa1 ^ xo1_step2)
        dom += chr(dom_byte)
        imul_iter = domain_length * step1
        imul_result = domain_length * imul_iter
        imul_1a = 0x1a * imul_result
        xor2 = xor1 ^ imul_1a
        xor1 = xor1 + xor2
        domain_length += 1

    domain_iterator += 1

    if add_tld:
        return dom + ".org", domain_iterator
    return dom, domain_iterator

def generate_domains(num_domains, seed_num=5, length=0x10):
    domains = []
    domain_iterator = 0
    for i in range(num_domains):
        domain, domain_iterator = generate_domain(seed_num, domain_iterator, length)
        domains.append(domain)

    return domains


# import ramdo
# ramdo.generate_domains(10, 5)
