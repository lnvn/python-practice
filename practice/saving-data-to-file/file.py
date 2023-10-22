man = []
other = []

try:
    data = open('liverpool.txt')
    try:
        for each_line in data:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Frodo':
                man.append(line_spoken)
            elif role == 'Sam':
                other.append(line_spoken)
    except ValueError:
        pass
    data.close()
except FileNotFoundError:
    print('File not found!')

print(f'man: {man}', end='\n')
print(f'other {other}', end='\n')
