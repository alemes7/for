import os

atletas = {}

s = 0

while s == 0:
    print("Escolha o que deseja realizar:")
    print("1 - Registro")
    print("2 - Alterar")
    print("3 - Listar")
    print("4 - Sair")
    
    x = input()
    
    if x == "1":
        nome = input("Nome do atleta: ")
        saltos = []
        for i in range(5):
            salto = float(input(f"Digite o valor do salto {i+1}: "))
            saltos.append(salto)
        atletas[nome] = saltos
        print("Registro concluído.")

#/////////////////////////////////////////////////////////////////////////////////////////////////

    elif x == "2":
        nome = input("Nome do atleta: ")
        if nome in atletas:
            saltos = atletas[nome]
            print(f"Saltos registrados: {saltos}")
            num_salto = int(input("Digite o número do salto que deseja alterar (1 a 5): "))
            if 1 <= num_salto <= 5:
                novo_salto = float(input("Digite o novo valor do salto: "))
                saltos[num_salto-1] = novo_salto
                atletas[nome] = saltos
                print("Alteração concluída.")
            else:
                print("Número de salto inválido.")
        else:
            print("Atleta não registrado.")

#////////////////////////////////////////////////////////////////////////////////////////////////////
        
    elif x == "3":
        if len(atletas) == 0:
            print("Nenhum atleta registrado.")
        else:
            print("Médias dos atletas:")
            for nome, saltos in atletas.items():
                media = sum(saltos) / 5
                print(f"{nome}: {media:.2f}")

#//////////////////////////////////////////////////////////////////////////////////////////////////////

    elif x == "4":
       s = 1

    else:
        print("Opção inválida.")

