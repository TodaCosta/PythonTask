
# def findThieves(message):
#     keywords = ['Edinaya Rossiya']
#     keywords2 = ['$', '¥', '€']
#     one = any(word in message.text for word in keywords)
#     two = any(word in message.text for word in keywords2)
#     return one and two

# text = input()
# d = ['карт', 'cvv']
# w = [g in text for g in d]
# print([g in text for g in d])
# print(w)
a = 'иран'
b = 'нари'
#print(a == b[::-1])
import re
message = 'Искать такси'
word = input()
def poli(message):
    message = re.sub(r'[ьъ]', '', message)
    message = message.lower().split()
    print(message)
    # for i in message:
    #     print(i == i[::-1])
    for i in range(len(message)):
        print(message[i] == message[i - 1][::-1])
    #print(message[0] == message[1][::-1])

def palindrom(word):
    word = word.replace(' ', '').lower()
    return word == word[-1::-1]
poli(message)
palindrom(word)