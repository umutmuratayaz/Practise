
""" 

İç içe listeler de içeren bir listenin elemanlarını tek bir listenin elemanı olacak şekilde düzenler.

1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, 
non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5] 
"""

input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


def flatten(input):
    for i in input:
        if type(i) == list:
            for j in flatten(i):
                yield j
        else:
            yield i
    


output = list(flatten(input))


print(output)



