def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida"


def modo_normal():
    print("=== CALCULADORA ===")

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(a, b, operacao)
    print("Resultado:", resultado)


def modo_de_teste():
    print("\n=== MODO DE TESTE (ESTRESSE) ===")

    minimo = int(input("Digite o valor mínimo: "))
    maximo = int(input("Digite o valor máximo: "))

    erros = 0

    for a in range(minimo, maximo + 1):
        for b in range(minimo, maximo + 1):

            if calculadora(a, b, '+') != a + b:
                print(f"Erro na soma: {a} + {b}")
                erros += 1

            if calculadora(a, b, '-') != a - b:
                print(f"Erro na subtração: {a} - {b}")
                erros += 1

            if calculadora(a, b, '*') != a * b:
                print(f"Erro na multiplicação: {a} * {b}")
                erros += 1

            if b != 0:
                if calculadora(a, b, '/') != a / b:
                    print(f"Erro na divisão: {a} / {b}")
                    erros += 1

                resultado = calculadora(a, b, '/')
                if resultado != "Erro: divisão por zero":
                    if calculadora(resultado, b, '*') != a:
                        print(f"Erro na contraprova da divisão: ({a}/{b})*{b} != {a}")
                        erros += 1

            soma = calculadora(a, b, '+')
            if calculadora(soma, b, '-') != a:
                print(f"Erro na contraprova da soma: ({a}+{b})-{b} != {a}")
                erros += 1

    if erros == 0:
        print("\nTodos os testes passaram com sucesso ✅")
    else:
        print(f"\nTotal de erros encontrados: {erros} ❌")


def menu():
    print("\nEscolha uma opção:")
    print("1 - Calculadora normal")
    print("2 - Modo de teste (estresse)")

    opcao = input("Opção: ")

    if opcao == '1':
        modo_normal()
    elif opcao == '2':
        modo_de_teste()
    else:
        print("Opção inválida")


if __name__ == "__main__":
    menu()
