fh = open("historicobaloto.txt", "r")
fo = open("historicobaloto2.txt", "w")
data = fh.readlines()
words = "["
for line in data:
	words += "\""+ line[:-2] +"\", "
words = words[:-2]
words += "]"
fo.writelines(words)
fo.close()
fh.close()
print words