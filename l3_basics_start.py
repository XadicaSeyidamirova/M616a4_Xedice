# # Dərs 3 · Blok 1 — Python-un 10 kərpici
# # İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# # Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# # Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# # ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

# print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# # TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)

# print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# # TODO: cell, rsrp, drops

# print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# # TODO: type(...) və «mətn ≠ ədəd»

# #name = input("Please enter your name: ")

# #print("my name", name, "my next age will be:", age + 1)
# #age = int(input("Please enter your age: "))
# #if age <25 :
#  #print(True)``
# #else:
#  #print(False)

# #print ( age > 25)
# #print ( age < 25)

# print("=== Kərpic 4 ===")   # Müqayisə → True / False
# # TODO: rsrp < -105, ==

# print("=== Kərpic 5 ===")   # Siyahı (list)
# # TODO: rsrp_list, indeks, len, orta


# # list verilib menim verdiyim index ile hemin indexdeki deyeri verir, 0-1e, 1-2e ve bu formada davam edir, eger 1 yazanda 1 olmasini isteyirikse, print(enodebs[antenna-1]) yazacaqyiq
# enodebs = ["GNJ0101", "GNJ9078", "GNJ9050", "GNJ3456", "GNJ4534", "GNJ2222"]
# antenna = int(input("Please enter index to show eNodeB: "))
# print(enodebs[antenna])
              

# print("=== Kərpic 6 ===")   # Lüğət (dict)
# # TODO: row = {...}, row["region"]

# # birinci ilkin formani yazir daha sonra dictricti deyisir yeni row a elave edir ve print edir
# row = {"cell id": "LLNK4545O5", "district": "Astara", "rsrp_dbm": -87}
# print(row)
# row["district"] = "Lerik"
# print(row)


# # key isteyir, yazdiqdan sonra qarisindaki valueni verir 
# #row = {"cell id": "LLNK4545O5", "district": "Astara", "rsrp_dbm": -87}
# key=(input("Please enter key to show your value:"))
# print(row[key])

# # deyisdirmek istediyimiz keyi isteyir daha sonra hemin keyin hansi value ile deyisdirmek istediyimizi qeyd edirik ve yeni row-u verir
# #row = {"cell id": "LLNK4545O5", "district": "Astara", "rsrp_dbm": -87}
# #key=input("Please enter key to change:")
# new_value = input("Please enter new value:")
# row[key] = new_value
# print(row)


# #rsrp_values = [ -96, -89, -90, -104, -113, -123]
# #entered_value = int(input("Please enter a number for looping: "))
# #for x in rsrp_values:
#     #print ( x * entered_value )

#  # print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# # TODO: zəif ölçmələri saymaq

# #rsrp_values = [ -96, -89, -90, -104, -113, -123, -130]
# weak = 0 
# for v in rsrp_values: 
#     if v >=-90:
#         print(v, "-> very high")
#     elif v>= -100:
#         print(v, "-> high")
#     elif v>= -105:
#         print(v, "-> normal")   
#     else :
#         print(v, "-> weak")
#         weak = weak + 1
# #print("zeif olcme sayi:", weak)

temp = float(input("Enter RRU TEMP. (C): "))

if temp > 0 and temp < 40:
        print(temp, "temperature is below freezing")
elif temp <=40 and temp >60:
       print(temp, "temperature is normal")
elif temp <=60:
        print(temp, "temperature is high")   
else :
        print(temp, "temperature is in critical level, ALERT!!!!")






print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd

# notes-



