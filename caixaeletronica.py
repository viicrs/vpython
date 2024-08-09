senha_correta = "1234"
nome = "Victoria"
for tentativa in range(3):
  senha = input( "Digite a senha: ")
  nome = input( "Digite o nome: ")
  if senha == senha_correta and nome == nome:
    print ("seja bem vindo ao nosso banco")
    break
  else:
    tentativas_restantes = 2 - tentativa
  if tentativas_restantes > 0:
    print(f"senha incorreta. Você tem {tentativas_restantes} tentativas   restantes.") 
  else:
   print("senha incorreta. Você        excedeu o número máximo de          tentativas.")
