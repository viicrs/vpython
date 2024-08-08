b = int(input("digite um numero: "))
a = int(input("digite um numero: "))

if(a < b):
  soma = 0
  for termo in range(a,b + 1):
      soma=soma+termo
  print(soma)

else:
  print("erro! tente novamente...")