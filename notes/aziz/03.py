s = input()
words = s.split()
maxi = len(words[0])
maxi_word = words[0]
for word in words:
	if maxi < len(word):
		maxi = len(word)
		maxi_word = word
# print (maxi_word)  Самое длинное слово и его номер
print (maxi)