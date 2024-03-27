import numpy as np

def generate_na_code(seq):
    na_code = np.zeros(len(seq) * 4)
    for i, base in enumerate(seq):
        if base == 'A':
            na_code[i * 4] = 1
        elif base == 'T':
            na_code[i * 4 + 1] = 1
        elif base == 'C':
            na_code[i * 4 + 2] = 1
        elif base == 'G':
            na_code[i * 4 + 3] = 1
    return na_code



