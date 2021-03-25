word = input("Give me a word, I wanna know if it\'s a palindrome: ")
if word[::-1] == word:
	print("This is a palindrome!")
else:
	print("This is not a palindrome :(")