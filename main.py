print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
liters = metros_quadrados / 3
cans = int(liters / 18)
if liters % 18 != 0 :
    cans += 1
# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = int(cans)
valor_total = int(qtd_de_latas * 80)

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")