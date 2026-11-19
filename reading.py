with open('new_file.txt', 'r') as file:
# file = open('new_file.txt')
    for line in file:
        print(line.strip())


# content = file.read(10)
# content = file.readline().strip()
# content = file.readlines()
# print(repr(content))
# print(content)
# content = file.readline()
# print(content)

# file.close
