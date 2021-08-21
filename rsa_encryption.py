#egcd and main function left

import random

def encrypt(e,N,msg):
  en = ""

  for c in msg:
    m = ord(c)
    en += str(pow(m,e,N)) + " "

  return en
  
def decrypt(d,N,msg):
  de = ""

  bits = msg.split()
  for bit in bits:
      if bit:
        m = int(bit)
      de += chr(pow(m,d,N))

  return de

def getkeys(size = 32):
  e = d = N = 0

  p = getLargePrime(size)
  q = getLargePrime(size)

  print(f'p : {p}')
  print(f'q : {q}')

  N = p *q

  #Euiler Totient
  t = (p-1) * (q-1)

  #public and private Keys
  e,d = numbersForEiler(t,size)

  return e,d,N

def numbersForEiler(t,size):
  while True:
    e= random.randrange(2**(size-1), (2**(size-1))**2)
    if isCoprime(e,t):
      break
  
  d = solved(e,t)

  return e,d

#choose large prime numbers
def getLargePrime(size):
  while True:
    num  = random.randint(2**(size-1), 2**size -1)
    if isPrime(num):
      return num


def isPrime(num):
  if num <2:
    return False

  #lowprime list
  primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
  
  if num in primelist:
    return True

  for i in primelist:
    if num%i == 0:
      return False

  c= num-1
  while c%2 == 0:
    c /= 2
  
  for i in range(128):
    if not rabinMiller(num,c):
      return False
    
  return True

def rabinMiller(num,d):
  a = random.randint(2,num-2)
  x= pow(a,int(d),num)
  if x == 1 or x == num - 1:
    return True

  while d != num - 1:
    x = pow(x, 2, num)
    d *= 2

    if x == 1:
      return False
    elif x == num - 1:
      return True

  return False

def isCoprime(a,b):
  return gcd(a,b)==1

def gcd(a,b):
  while b:
    a,b = b,a%b
  return a

def egcd(a,b):
  s = 0; old_s = 1
  t = 1; old_t = 0
  r = b; old_r = a

  while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    old_t, t = t, old_t - quotient * t

  # return gcd, x, y
  return old_r, old_s, old_t

def solved(e,t):
  gcd,x,y = egcd(e,t)

  if x<0:
    x += t

  return x

def main():

  keysize = 32
  while True:
    strength = int(input('\nChoose Encryption Strngth : \n1. Low\n2. Medium\n3.High\n'))
    if strength == 1:
      keysize = 32
    elif strength == 2:
      keysize = 64
    elif strength == 3:
      keysize = 128
    else:
      print('Enter valid choice.')

    e,d,N = getkeys(keysize)

    msg = input('Enter the secret : ')

    en = encrypt(e,N,msg)
    de = decrypt(d,N,en)

    print(f"Message: {msg}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"N: {N}")
    print(f"enc: {en}")
    print(f"dec: {de}")

    choice = input('Enter another secret ? [y/n] : ')
    if choice == 'N' or choice == 'n':
      break

main()