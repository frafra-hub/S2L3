nome_città= str(input("Inserisci il nome della tua città di origine: "))
nome_animale=str(input("Inserisci il nome del tuo animale domestico: "))
vocali=["a","e","i","o","u"]
nome_cit=nome_città[:-1]
while (nome_cit[len(nome_cit)-1] not in vocali):
    nome_cit=nome_cit[:-1]
nome_an=nome_animale[1:]
while (nome_an[0] in vocali):
    nome_an=nome_an[1:]
nome_band=nome_cit+nome_an
print ("Il nome della tua band è",nome_band.upper())
