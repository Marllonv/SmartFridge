
lista_usuario = []
lista_cartoes = []
lista_carrinho = []

def entrar_usuario(email, senha):
    for usuario in lista_usuario:
        if usuario['email'] == email and usuario[senha] == senha:
            print(f"Usuário {usuario[usuario]} logado com sucesso!")
            return True
    return False

def adicionar_carrinho(nome, id):
    novo_produto = {
            "nome": nome,
            "id": id
        }
    lista_carrinho.append(novo_produto)

def adicionar_cartao(numero, titular, validade, cvv):
  novo_cartao = {
    "numero": numero,
    "titular": titular,
    "validade": validade,
    "cvv": cvv
  }
  lista_cartoes.append(novo_cartao)
  
def adicionar_usuario(email, usuario, senha, confirmasenha):
    if senha == confirmasenha:
        novo_usuario = {
            "email": email,
            "usuario": usuario,
            "senha": senha
        }
        lista_usuario.append(novo_usuario)
    else:
        print("Erro ao confirmar senha.")
        
def trocar_senha(email):
    for usuario in lista_usuario:
        if usuario["email"] == email:
            usuario["senha"] = int(input("Nova senha"))
            return True

    return False
            
def realizar_compra():
    print("Compra realizada com sucesso! Itens comprados:")
    print(lista_carrinho)
    lista_carrinho = []
     
# while True:
#     opcao = 0
#     print("Escolha uma opção:")
#     opcao = int(input())
#     if opcao == 1:
#         entrar_usuario
#         (
#             input("Digite seu email: "),
#             input("Digite sua senha: ")
#         )
        
#     elif opcao == 2:
#         adicionar_usuario
#         (
#             input("Digite seu email: "),
#             input("Digite seu usuário: "),
#             input("Digite sua senha: "),
#             input("Confirme sua senha: ")
#         )
#     elif opcao == 3:
#         trocar_senha
#         (
#             input("Digite seu email: ")
#         )
#     elif opcao == 4:
#         adicionar_cartao
#         (
#             input("Digite o número do cartão: "),
#             input("Digite o nome do titular do cartão: "),
#             input("Digite a validade do cartão: "),
#             input("Digite o código cvv do cartão: ")
#         )
#     elif opcao == 5:
#         adicionar_carrinho
#         (
#             input("Digite o nome do produto: "),
#             input("Digite o ID do produto: ")
#         )
#     elif opcao == 6:
#         print("Os produtos no carrrinho são:")
#         print(lista_carrinho)
#     elif opcao == 7:
#         realizar_compra
#         ()
#     elif opcao == 0:
#         break
