#frase escolhida
text = input("What is your phrase?\n> ")

#dicionário
dic = {}

#para cada caracter da frase
for i in text:
    #se o caracter for um espaço, ignorar
    if i == " ":
        continue
    
    #se á primeira vez q o i aparece(valor = 0)
    #adiciona 1 ao valor
    #se já existe, é o valor atual + 1
    dic[i] = dic.get(i, 0) + 1

print(dic)