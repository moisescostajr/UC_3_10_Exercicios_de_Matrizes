#3. Solicite ao usuário os valores de uma matriz 3x3. Ao final exiba a matriz completa.

matriz = []
for i in range(3):
    nova = []
    for j in range(3):
        valor = int(input(f"Digite um valor inteiro para a posição [{i}][{j}]: "))
        nova.append(valor)

    matriz.append(nova)
    
print(matriz)