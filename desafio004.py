a = input("Digite algo")
print(type(a))
print("tem espaço?", a.isspace()) # confere se tem espaço

if a.isdigit():  # converte se for um número
    a = int(a)
    print("Agora é um número:", type(a))
