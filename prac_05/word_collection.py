import re

dict = {}
sentence_list = input('Please enter a sentence: ')
#sentence_list = ['This is a sentence', 'This is a sentence']
#print(sentence_list)
#for sentence in sentence_list:
for word in re.split('\s', sentence_list): # split with whitespace
    try:
        dict[word] += 1
    except KeyError:
        dict[word] = 1
#print (dict[0], dict[1])1

for i in sorted(dict):
    print('{} : {}'.format(i, dict[i]))