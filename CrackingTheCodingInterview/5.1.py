def insertion(n, m, i, j):
 
    clear_mask = -1 << (j + 1)
    print(clear_mask, bin(clear_mask))
    capture_mask = (1 << i) - 1
    print(capture_mask, bin(capture_mask))
    # Capturing bits from i-1 to 0
    captured_bits = n & capture_mask
    print(captured_bits, bin(captured_bits))
    # Clearing bits from j to 0
    n &= clear_mask
    print(n, bin(n))
    # Shifting m to align with n
    m = m << i
 
    # Insert m into n
    n |= m
 
    # Insert captured bits
    n |= captured_bits
 
    return n
 

N = 1201; M = 8; i = 3; j = 6
print("N = {}({})".format(N, bin(N)))
print("M = {}({})".format(M, bin(M)))
N = insertion(N, M, i, j)
print("***After inserting M into N***")
print("N = {}({})".format(N, bin(N)))