#7. Solicite os valores de uma matriz 3x3 e calcule a soma da diagonal principal.

matriz = []
soma_diagonal = 0

for i in range(3):
    elementos = []
    for j in range(3):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        elementos.append(valor)

        if i == j:
            soma_diagonal += valor

    matriz.append(elementos)

print("\nMatriz informada:")
for elementos in matriz:
    print(elementos)

print(f"\nSoma da diagonal principal: {soma_diagonal}")