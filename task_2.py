with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    # print(f.read())
    b = []
    for line in f:
        # print(line[:line.find(' - - ')], line[line.find('"') + 1:line.find(' /')],
        #       line[line.find(' /') + 2:line.find('" ')])
        b.append(
            fr"{line[:line.find(' - - ')]}, {line[line.find('\"') + 1:line.find(' /')]}, {line[line.find(' /') + 2:line.find('\" ')]}")
        # b.append(line[:line.find(' - - ')])
        # b.append(line[line.find('"') + 1:line.find(' /')])
        # b.append(line[line.find(' /') + 2:line.find('" ')])
    print(b)
# a = ('80.91.33.133', 'GET', 'downloads/product_1 HTTP/1.1')
# print(type(a))
