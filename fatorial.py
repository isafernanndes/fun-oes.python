def fatorial(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    

numero = int(input('digite um número: '))
print(f'fatorial de {numero} = {fatorial(numero)}')