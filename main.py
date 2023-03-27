print("🌟 MAGCALC 1.0 🌟\nEssa é uma calculadora magnífica, vamos lá!")

while True:
    while True:
        try:
            valor1 = int(input("\n🔢 Informe um número: "))
            break
        except ValueError:
            print("Informe um número inteiro.")
    while True:
        try:
            valor2 = int(input("🔢 Informe outro número: "))
            break
        except ValueError:
            print("Informe um número inteiro.")

    soma = valor1 + valor2
    subtracao = valor1 - valor2
    divisao = valor1 / valor2
    multiplicacao = valor1 * valor2

    print("\n====================\n")
    print("+ A soma de {} mais {} é: {}".format(valor1, valor2, soma))
    print("- A subtração de {} menos {} é: {}".format(valor1, valor2, subtracao))
    print("/ A divisão de {} por {} é: {:.2f}".format(valor1, valor2, divisao))
    print("* A multiplicação de {} por {} é: {}".format(valor1, valor2, multiplicacao))
    print("\n====================\n")

    repetir = input("Deseja continuar na MAGCALC? (S/N)")

    # Se a resposta do usuário for "N", sai do loop
    if repetir.upper() == "N":
        print("\n========== OBRIGADO E VOLTE SEMPRE ==========\n")
        break
