"""

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 

Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

"""

input = [[1, 2], [3, 4], [5, 6, 7]]

def reverseList(input):
    input.reverse()
    for i in input:
        if type(i) == list:
            reverseList(i)

reverseList(input)

print("Reversed Input: ", input)
    