# MEGA SENA GENERATOR
# Um script simples para gerar um arquivo CSV com apostas aleatórias da Mega Sena

# importa biblioteca para gerar sequencias aleatórias
import random

# solicita número de apostas ao usuário
numero_de_apostas = int(input('\nQuantas apostas quer gerar? > '))

# função para gerar uma aposta
def gera_aposta():
    
    # cria lista com números 1 a 60 no voltante da aposta
    volante = list(range(1,61))
    
    # cria lista para armazenar números da aposta
    aposta = []
    
    # gera a aposta com 6 números
    for i in range(6):
        
        # escolhe um número aleatório do volante
        random_item = random.choice(volante)
        
        # adiciona o número à lista que compõe a aposta
        aposta.append(random_item)
        
        # remove o número do volante (para não escolher número repetido)
        volante.remove(random_item)
        
        # coloca os números em ordem crescente
        aposta.sort()
    
    #entrega os números da aposta
    return aposta

# cria lista para armazenar todas as apostas
apostas = []

# loop para criar o número de apostas desejado
for i in range(numero_de_apostas):
    
    # evoca a função que gera a aposta
    apostas.append(gera_aposta())

# cria string para armazenar números das aposas
csv_string = ''

# loop insere os números dessas apostas no string
for aposta in apostas:
    
    # coloca vírgulas entre os números
    for number in aposta:
        csv_string = csv_string + str(number) + ','
    
    # coloca uma aposta em cada linha
    csv_string = csv_string + '\n'

# ajusta formatação do string para eliminar espaços vazios e vírgulas extra
csv_string = csv_string.replace(',\n', '\n').strip()

# salva as apostas em um arquivo csv
with open('apostas.csv', 'w') as file:
    file.write(csv_string)