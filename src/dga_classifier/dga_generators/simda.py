# Original: https://github.com/baderj/domain_generation_algorithms/blob/master/simda/dga.py
def generate_domains(nr_domains, length=10, tld="com", key = "1676d5775e05c50b46baa5579d4fc7", base = 0x45AE94B2):
    consonants = "qwrtpsdfghjklzxcvbnmv"
    vowels = "eyuioa"

    step = 0
    for m in key:
        step += ord(m)

    ret = []

    for nr in range(nr_domains):
        domain = ""
        base += step

        for i in range(length):
            index = int(base/(3+2*i))
            if i % 2 == 0:
                char = consonants[index % 20]
            else:
                char = vowels[index % 6]
            domain += char

        if tld:
            domain += "." + tld
        
        ret.append(domain)

    return ret