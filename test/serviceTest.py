services = []
with open("../files/Local Service.txt") as file:
    for line in file:
        line = line.strip('\n')
        line = line.strip(' ')
        services.append(line)
