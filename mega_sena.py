volante = list(range(1,61))
aposta = []
for i in range(6):
    random_item = random.choice(volante)
    aposta.append(random_item)
    volante.remove(random_item)
    aposta.sort()
print(aposta)