# Number the lines in the file

text = open("11.txt", "r")
lines = text.readlines()
text.close()

text = open("11.txt", "w")
num = 156
for line in lines:
    text.write("{0:03d}".format(num) + line)
    num = num + 1
text.close()
