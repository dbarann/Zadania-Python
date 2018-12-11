my_file=open('plik.txt', 'a')
my_file.write('dodajemy tekst')
my_file.close()
print (open('plik.txt').read())