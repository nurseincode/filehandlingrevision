file = open('new_file.txt')
# content = file.read()
# content = file.readline().strip()
content = file.readlines()
# print(repr(content))
print(content)
# content = file.readline()
# print(content)

file.close
