#5. Solicite os valores de uma matriz 3x3 e encontre o maior valor.

matriz = []
maior_valor = 0

for i in range(3):
    elementos = []
    for j in range(3):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        elementos.append(valor)

        if maior_valor is None or valor > maior_valor:
            maior_valor = valor

    matriz.append(elementos)

print("\nMatriz informada:")
for linha in matriz:
    print(elementos)

print(f"\nMaior valor da matriz: {maior_valor}")