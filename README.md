# tugas-algoritma-1.py
# hasil penjumlahan kelipatan 3 & 5 > 1000
sum3 = 0 
sum5 = 0

i = 3
while i < 1000:
    sum3 += i 
    i += 3

j = 5
while j < 999:
    sum5 += j
    j += 5
    print(sum3+sum5)
