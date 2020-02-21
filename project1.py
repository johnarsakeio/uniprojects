import re 
string = open('test.txt').read()#name file to be worked with to test for this to work
new_str = re.sub('[^άέώύήίόΆΏΈΎΊΌΉα-ωΑ-Ωa-zA-Z0-9\n]', ' ', string)
open('b.txt', 'w').write(new_str)
with open('b.txt') as f:
    word_list=[word for line in f for word in line.split()]
word_list.sort(key=len, reverse=True)
vowels = ('a', 'e', 'i', 'o', 'u','α','ω','ε','υ','η','ι','ο','ά','έ','ώ','ύ','ή','ί','ό')
if len(word_list)>=5:
    for x in range(4):
        for y in word_list[x]:
            if y in vowels:
                word_list[x] = word_list[x].replace(y,"")
        print (word_list[x][::-1],',')
else:
    for x in range(len(word_list)-1):
        for y in word_list[x]:
            if y in vowels:
                word_list[x] = word_list[x].replace(y,"")
        print (word_list[x][::-1],',')

