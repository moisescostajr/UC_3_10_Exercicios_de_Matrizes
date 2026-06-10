#4. Solicite os valores de uma matriz 3x3 e calcule a soma de todos os elementos.

matriz = []
soma = 0

for i in range(3):
    elementos = []
    for j in range(3):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        elementos.append(valor)
        soma += valor
    matriz.append(elementos)

print("\nMatriz informada:")
for elementos in matriz:
    print(elementos)

print(f"\nSoma de todos os elementos é: {soma}")
