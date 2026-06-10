#6. Solicite os valores de uma matriz 3x3 e exiba apenas os elementos da diagonal principal.

matriz = []

for i in range(3):

    elementos = []
    for j in range(3):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        elementos.append(valor)
    matriz.append(elementos)

print("\nElementos da diagonal principal:")
for i in range(3):
    print(matriz[i][i])