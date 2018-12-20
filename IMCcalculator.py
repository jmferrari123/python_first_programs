print("calculadora de IMC")
altura = float(input("Informe a altura em metros.")) #(primeiro programa em py :3)
massa = float(input("Informe a massa em Kilogramas."))

IMC = (massa) / (altura * altura)

if IMC <  18.5:
    print("Abaixo do peso com IMC menor do que 18.5.")
    print("E seu IMC é :")
    print(IMC)
elif IMC > 25:
    print("Acima do peso com IMC maior do que 18.5.")
    print("E seu IMC é :")
    print(IMC)
else :
    print("IMC normal.")
    print("E seu IMC é :")
    print(IMC)