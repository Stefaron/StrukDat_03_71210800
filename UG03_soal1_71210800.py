kalimat = input('Masukkan kalimat : ')
kata = input('Masukkan kata yang ingin dicari : ')

jumlah = 0
kata = kata.lower()
kalimat = kalimat.lower().split()
for i in kalimat:
    if i == kata:
        jumlah += 1

print(jumlah)