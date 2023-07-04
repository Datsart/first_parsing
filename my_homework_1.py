with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    part_1 = []
    part_2 = []
    part_3 = []
    for line in f:
        if line[0:line.find(' -')] in line:
            part_1.append(line[0:line.find(' -')])
            if line[line.find(' "') + 2:line.find(' /')] in line:
                part_2.append(line[line.find(' "') + 2:line.find(' /')])
                if line[line.find(' /') + 2:line.find('" ')] in line:
                    part_3.append(line[line.find(' /') + 2:line.find(' H')])

total = list(zip(part_1, part_2, part_3))
for i in total:
    print(i)