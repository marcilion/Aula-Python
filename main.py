#from datetime import datetime
import calculadora

#from calculadora import somar, subtrair, multiplicar, dividir

#import calculadora as funcoes


#print(calculadora.somar(5,10))

#print(calculadora.subtrair(5,10))

#print(calculadora.multiplicar(5,10))

#print(calculadora.dividir(5,10)) 

possiveis_opcoes = ["1", "2", "3", "4", "5"]
opcao = ""
while opcao != "5":
print(" 1 - somar\n2 - subtrair\n3 - multiplica\n4 - dividir\n5 - sair")
opcao = input("Digite uma opção: ")


try: 
    opcao_valida = possiveis_opcoes.index(opcao) > -1
except ValueError:
    print("Opção inválida")
    opcao_valida = False
except Erro:
    print("Erro inesperado")
    opcao_valida = False

if opcao_valida == True and opcao != "5":
    numero1 = int(input("Digite o primeiro número: "))    
    numero2 = int(input("Digite o Segundo número: "))

    resultado = 0
    if opcao == '1':
        resultado = calculadora.somar(numero1, numero2)
    elif opcao == '2':
        resultado = calculadora.subtrair(numero1, numero2)
    elif opcao == '3':
        resultado = calculadora.multiplicar(numero1, numero2)
    elif opcao == '4':
        resultado = calculadora.dividir(numero1, numero2) 
    elif opcao == '5':
        print("sair")   

if opcao == "5":

    exit()

else:
    numero1 = int(input("Digite o primeiro número:  "))
    jls_extract_var = input
    numero2 = int(jls_extract_var("Digite o segundo número: "))


    resultado = 0

    if opcao == '1':

        resultado = calculadora.somar(numero1, numero2)

    elif opcao == '2':

        resultado = calculadora.subtrair(numero1, numero2) 

    elif opcao == '3':

        resultado = calculadora.multiplicar(numero1, numero2)

    elif opcao == '4':

        resultado = calculadora.dividir(numero1, numero2)


print(f"Resultado:{resultado}")