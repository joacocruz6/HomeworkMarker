def fib(n):
     if n == 0 or n==1: 
          return 1
     else:
          return fib(n-1)+fib(n-2)
def main(args):
     name = int(input(""))
     numero = fib(name)
     print(numero)
if __name__ == "__main__":
     main([])