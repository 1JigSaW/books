from utils.binutils import blen

def insertBit(N, M, i, j):
    len_n = blen(n)
    len_m = blen(m)

    mask = 0b1 << (len_n - j - 1)
    mask -= 1
    # print(f"Mask is\t{mask:b}")

    mask <<= j + 1
    # print(f"Mask is\t{mask:b}")

    mask += (0b1 << i+1) - 1
    # print(f"Mask is\t{mask:b}")
    # print(f"N is\t{n:b}")
    n &= mask
    print(f"N is\t{n:b}")

    j_mask = m << i
    # print(f"Jmask is\t{j_mask:b}")
    n |= j_mask
    return n

N = 0b10000000000
M = 0b10011
i = 2
j = 6

print(insertBit(N, M, i, j))