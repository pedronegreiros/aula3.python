# usuario = {
#     "nome": str(input("digite seu nome: ")),
#     "sobrenome": str(input("digite seu sobrenome: ")),
#     "idade": int(input("digite sua idade: ")),
#     "email": str(input("digite seu email: ")),
# }

# print(f"""
#       1 - {usuario["nome"]}
#       2 - {usuario['sobrenome']}
#       3 - {usuario['idade']}
#       4 - {usuario['email']})
# """)

lista_de_notas = []
maior_nota = 0
soma = 0
meno_nota = float("inf")

for i in range (1,5):
    nota = float(input(f"digite {i} nota: "))

    lista_de_notas.append(nota)

    if nota > maior_nota:
        maior_nota = nota

media = soma / len(lista_de_notas)

if media>=7:
   
    aprovado = "aprovado"

