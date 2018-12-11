delete = ["sie", "i", "oraz", "nigdy", "dlaczego"]
f_in = open("file.txt")
f_out = open("outfile.txt", "w+")
for line in f_in:
    for word in delete:
        line = line.replace(word, "")
    f_out.write(line)
f_in.close()
f_out.close()