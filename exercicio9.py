#9. Solicite os valores de uma matriz 3x3 e calcule a média dos elementos

matriz = []
soma = 0

for i in range(3):
    elementos = []
    for j in range(3):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        elementos.append(valor)
        soma += valor
    matriz.append(elementos)

media = soma / 9

print("\nMatriz informada:")
for elementos in matriz:
    print(elementos)

print(f"\nMedia dos elementos: {media}")