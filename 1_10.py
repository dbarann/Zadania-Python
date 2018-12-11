dict =	{
  "i": "oraz",
  "oraz": "i",
  "nigdy": "prawie nigdy",
  "dlaczego": "czemu"
}
f_in = open("file.txt")
f_out = open("outfile.txt", "w+")
for line in f_in:
    for word in dict:
        line = line.replace(word, dict[word])
    f_out.write(line)
f_in.close()
f_out.close()		