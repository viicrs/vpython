soma = 0
quant = 0
menor = 0
nome = ""

for i in range(5):
  n = input("digite o nome do medicamento: ")
  p = float(input("digite o preço do medicamento: "))

  soma += p
  quant += 1

  if p < menor:
    menor = p
    nome  = n

    media  = soma / quant
    print(f"o medicamento mais barato é: '{n}'  com preço d R${menor:.2f}")
    print("a media dos preços é: {media:.2f}")
