import math

def quadrado(num):
    raiz = int(math.sqrt(num))
    return raiz * raiz == num

def fibo(num):
    return quadrado(5 * num * num + 4) or quadrado(5 * num * num - 4)

numero = int(input("Informe um número: "))

if fibo(numero):
    print(f" {numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

