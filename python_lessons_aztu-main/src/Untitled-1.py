library = {
    "Riyaziyyat": 3,
    "Fizika": 0,
    "Informatika": 4
}
for fenn, say in library.items():
    if say > 0:
        print(f"{fenn}: {say}")
butun_nusxe_sayi = sum(library.values())
print( butun_nusxe_sayi)
kitab=int(input())              

maaslar = {
    "A": 900,
    "B": 1200,
    "C": 7000,
    "D": 800
}
orta_maas = sum(maaslar.values()) / len(maaslar)

print(orta_maas)