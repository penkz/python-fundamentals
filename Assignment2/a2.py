def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1) > len(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    return dna.count(nucleotide)



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1

def is_valid_sequence(dna):
    '''(str) -> bool

    Return True if and only if the DNA sequence is valid.

    >>> is_valid_sequence('ACGTACG')
    True
    >>> is_valid_sequence('TCATGT')
    True
    >>> is_valid_sequence('TCGABAKV')
    False
    >>> is_valid_sequence('zxcvbnmk')
    False
    '''
    nucleotides = 'AGCT'
    valid = True

    if dna == '': return True
    if not dna.isupper(): return False
    
    for nucleotide in dna:
        if nucleotide not in nucleotides:
            valid = False
    return valid

def insert_sequence(dna1,dna2,index):
    '''(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA
    sequence into the first at the given index.

    Assuming the index is valid.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ACTGAGC','ACGT', -2)
    'ACTGAACGTGC'
    
    '''
    dna3 = dna1[:index] + dna2 + dna1[index:]
    return dna3


def get_complement(nucleotide):
    '''(str) -> str

    Return the nucleotide's complement

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    '''
    complement = ''
    
    if nucleotide == 'A':
        complement = 'T'
    elif nucleotide == 'T':
        complement = 'A'
    elif nucleotide == 'C':
        complement = 'G'
    else:
        complement = 'C'

    return complement

def get_complementary_sequence(sequence):
    '''(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    >>> get_complementary_sequence('GCATCGTA')
    'CGTAGCAT'
    '''

    complementary_sequence = ''
    
    for nucleotide in sequence:
        complementary_sequence += get_complement(nucleotide)

    return complementary_sequence

if __name__ == '__main__':
    import doctest
    doctest.testmod()