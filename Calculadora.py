while True:
    numero_1 = input("Digite o primeiro número:  ")
    numero_2 = input("Digite o segundo número:  ")
    operador = input("Digite o operador (+, -, *, /): ")
    
    numeros_validos = True

    try:
        num1 = float(numero_1)
        num2 = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print("Operador inválido. Por favor, use +, -, * ou /.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando sua conta...")

    if operador == '+':
            resultado = num1 + num2
    elif operador == '-':
            resultado = num1 - num2
    elif operador == '*':
            resultado = num1 * num2
    elif operador == '/':
        continue
            
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        continue
    
    resultado = num1 / num2
    
        

    print(f"O resultado de {num1} {operador} {num2} é: {resultado}")

    sair = input("Deseja sair do programa? [s]im?  ").lower().startswith('s')
    if sair is True:
        break