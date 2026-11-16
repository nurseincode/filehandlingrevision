# Open a file for writing - destructive - overwrites existing content
# file = open('new_file.txt', 'w')
file = open('new_file.txt', 'a')

file.write('This is a new file\n')
file.write('See ya!\n')

file.close()