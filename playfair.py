#!/usr/bin/python3
'''
Playfair Cipher Implementation
Brandon Asuncion
brandonasuncion@gmail.com
'''

import string
	
def playfair(key, inputfile, outputfile, encrypting=True):
	
	def pos(row, col):				# given a row/column, get the position in the table string
		return row * 5 + col
	
	def cell(position):				# given a position in the table string, get the row/column
		row = int(position / 5)
		col = position % 5
		return row, col
	
	with open(inputfile, 'r') as fh:
		remaining = fh.read().lower()
	
	table = ""
	
	# add the key & alphabet to the matrix; ignore duplicates
	for c in key.lower() + string.ascii_lowercase:
		if c in ['i', 'j']:		# treat i/j as the same char
			if ('i' not in table) and ('j' not in table):
				table = table + 'i'
		elif c not in table:
			table = table + c
	
	cipher = ""
	while remaining != "":
		
		# if only 1 character is left
		if len(remaining) == 1:
			a = remaining[0]
			b = "x"
			remaining = ""
			
		# duplicate letter
		elif remaining[0] == remaining[1]:
			a = remaining[0]
			b = "x"
			remaining = remaining[1:]
			
		else:
			a = remaining[0]
			b = remaining[1]
			remaining = remaining[2:]
			
		# replace j's with i's
		a = "i" if a == "j" else a
		b = "i" if b == "j" else b
		
		c1 = cell(table.find(a))
		c2 = cell(table.find(b))
		
		shift = 1 if encrypting else -1	# for same column/row; if encrypting shift +1, else shift -1
		
		if c1[0] == c2[0]:		# same row
			cipher = cipher + table[pos(c1[0], (c1[1]+shift) % 5)] + table[pos(c2[0], (c2[1]+shift) % 5)]
		elif c1[1] == c2[1]: 	# same column
			cipher = cipher + table[pos((c1[0]+shift) % 5, c1[1])] + table[pos((c2[0]+shift) % 5, c2[1])]
		else:
			cipher = cipher + table[pos(c1[0], c2[1])] + table[pos(c2[0], c1[1])]
	
	with open(outputfile, 'w') as fh:
		fh.write(cipher)
		
	return cipher
	
playfair("monarchy", "test.txt", "cipher.txt", True)
playfair("monarchy", "cipher.txt", "plaintext.txt", False)