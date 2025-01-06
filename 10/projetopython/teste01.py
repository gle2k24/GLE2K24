print("ola, mundo, testandoo python!")

# variaveis e tipos basicos 
nome = "Maria"
idade = 25
altura = 1.68
esta_estudando = True 

print(nome, idade, altura, esta_estudando)

nome = input("Digite seu nome: ")
print("Ola", nome,"seja bem-vindo!" )

#soma de dois numeros
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

soma = num1 + num2
print("A soma e:",soma)

numero = int(input("Digite um numero:"))

if numero % 2 == 0:
    print("O numero e par.")
else:
    print("O numero e impar.")
