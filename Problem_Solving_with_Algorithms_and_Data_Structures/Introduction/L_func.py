def square(n):
	return n**2

print(square(3))

print(square(square(3)))


def squareroot(n):
    root = n/2    #первоначальная догадка должна составлять 1/2 от n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root

print(squareroot(9))

print(squareroot(4563))