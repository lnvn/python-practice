data = open('liverpool.txt')

try:
    for each_line in data:
        role, line_spoken = each_line.split(':')
        print(role, end='')
        print(" Said: ", end='')
        print(line_spoken)
except: pass