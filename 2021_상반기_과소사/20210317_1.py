a = 23
b = 5

print('a(2) = ',bin(a))
print('b(2) = ',bin(b))
print()

print('a & b = ', a & b, 'Binaty = ', bin(a & b))
print('b & a = ', b & a, 'Binaty = ', bin(b & a))
print('a | b = ', a | b, 'Binaty = ', bin(a | b))
print('b | a = ', b | a, 'Binaty = ', bin(b | a))
print('a ^ b = ', a ^ b, 'Binaty = ', bin(a ^ b))
print('b ^ a = ', b ^ a, 'Binaty = ', bin(b ^ a))
print('~a = ', ~a, 'Binaty = ', bin(~a))
print('~b = ', ~b, 'Binaty = ', bin(~b))
print()

print('a << b : ', a << b, 'Binaty = ', bin(a << b))
print('a >> b : ', a >> b, 'Binaty = ', bin(a >> b))
print('b << a : ', b << a, 'Binaty = ', bin(b << a))
print('b >> a : ', b >> a, 'Binaty = ', bin(b >> a))
print()

c = 1024
print('11th bit of %d :' %c, 1 & (c >> 10))
print()

d = 4
print('1st bit of %d : ' %d, 1 & (d >> 0))
print('2st bit of %d : ' %d, 1 & (d >> 1))
print('3st bit of %d : ' %d, 1 & (d >> 2))
print()

e = 13
print('1st bit of %d : ' %e, 1 & (e >> 0))
print('2st bit of %d : ' %e, 1 & (e >> 1))
print('3st bit of %d : ' %e, 1 & (e >> 2))
print('4st bit of %d : ' %e, 1 & (e >> 3))