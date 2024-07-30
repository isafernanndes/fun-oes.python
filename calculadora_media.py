def calcular_media():
    notas = []
    print('Digite as notas (digite sair para terminar):')

    while True:
        entrada = input()
        if entrada.lower() == 'sair':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print('Por favor, digite uma nota entre 0 e 10')
        except ValueError:
            print('Por favor, digite um número válido')

    if notas:
        media = sum(notas) / len(notas)
        print(f'A média das notas é: {media:.2f}')
    else:
        print('Nenhuma nota foi inserida')

calcular_media()
