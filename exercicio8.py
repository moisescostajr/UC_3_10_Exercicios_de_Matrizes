#8. Solicite os valores de uma matriz 4x4 e informe quantos números pares existem.

matriz = []
pares = 0

for i in range(4):
    elementos = []
    for j in range(4):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        elementos.append(valor)

        if valor % 2 == 0:
            pares += 1

    matriz.append(elementos)

print("\nMatriz informada:")
for elementos in matriz:
    print(elementos)

print(f"\nQuantidade de numeros pares: {pares}")