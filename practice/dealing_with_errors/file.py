data = open('liverpool.txt')

try:
    for each_line in data:
        # use split(":",1) to handle issue if we have another colon in line_spoke
        role, line_spoken = each_line.split(':')
        print(role, end='')
        print(" Said: ", end='')
        print(line_spoken)
except:
    print("Hello World")