# Creando la serie de fibonacci

def fib(num):
   a,b = 0,1
   fibo_list = [0]
   for i in range(num):
     if b > num: return fibo_list
     else:   
      fibo_list.append(b)
      a,b = b,a+b



resultado = fib(34) 
print(resultado)

primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5)+1)),range(2,num)))

print(primos_hasta(20))