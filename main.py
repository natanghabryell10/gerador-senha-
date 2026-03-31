import random
import string

tamanho = 16
caracteres = string.ascii_uppercase + string.digits

senha = ''.join(random.choice(caracteres) for i in range(tamanho))

print("Senha gerada:", senha)
