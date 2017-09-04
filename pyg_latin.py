import msvcrt

print "Welcome to Pyg Latin"
print ""

pyg = 'ay'

original = raw_input('Enter a word: ')
print ""

if len(original) > 0 and original.isalpha():
  print "Original word: " + original
else:
  print 'empty'

print ""
word = original.lower()
first = word[0]
new_word = word + first + pyg

new_word = new_word[1:len(new_word)]

print "Pyg Latin Translation: " + new_word
print ""
print "Pulse cualquier tecla para salir."
while True:
	if msvcrt.kbhit():
		break
