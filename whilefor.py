import os

#Variaveis
Lista = "1"
Frutas = "2"
Chamada = "3"
sim = "y"
não = "n"

print("Menu simples")
print("[1] Lista 10 números")
print("[2] 5 frutas")
print("[3] Chamada")
print("")
a = input("Digite a função que deseja:")

s = 1
while s == 1:

    if a == Lista:
        s = 1
        print("Lista 10 números")
        print("")

        num = [120,220,320,420,520,620,720,820,920,1020]

        for N in num:
            print(N)

        print("Você deseja sair:")
        print("Sim [y]")
        print("Não [n]")

        z=(input(""))

        if z == sim:
            s = 0
        elif z == não:
            S = 1
        else:
            print(" ")
            print("Código invalido")
            print(" ")

        if a == Frutas:
            s = 1
            print("")
            print("5 frutas")
            print("")

            F=["Maçã", "Morango", "Uva", "Melancia", "Caju"]

            for FR in F:
                print(FR)
    
            else:
                print(" ")
                print("Código invalido")
                print(" ")

                print("Você deseja sair:")

                z=(input(""))

                if z == sim:
                    s = 0
                elif z == não:
                    S = 1
                else:
                    print(" ")
                    print("Código invalido")
                    print(" ")

                if a == Chamada:
                    s = 1
                    print("")
                    print("Chamada de 1 a 34")
                    print("")

                    C = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
                    for ch in C:
                        print(ch)
                    else:
                        print(" ")
                        print("Código invalido")
                        print(" ")

                        print("Você deseja sair:")

                        z=(input(""))

                        if z == sim:
                            s = 0
                        elif z == não:
                            S = 1
                        else:
                            print(" ")
                            print("Código invalido")
                            print(" ")

os.system("Pause")