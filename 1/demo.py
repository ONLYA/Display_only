# python 3.8.0

from time import time

def test1():
 abc = time()
 a = 11
 if a < 12:
  print(a)
 return time()-abc

def test2():
 abc = time()
 if (b:=11) < 12:
  print(b)
 return time()-abc

def total_test(num):
 r1 = 0;r2 = 0
 for i in range(num):
  r1 += test1()
  r2 += test2()
 print("Test 1: {}\nTest 2: {}".format(r1/num, r2/num))

def main():
 while True:
  total_test(10000)
  input("Press to continue...")

if __name__ == '__main__':
 main()
