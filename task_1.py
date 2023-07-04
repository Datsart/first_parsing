# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     print(f)


# открыли файл в режиме на запись, и записали строку.
# При каждом запуске создается новый файл и старые данные стираются!!!
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!')

# режим r+ - это режим редактирования и курсор устанавливается в начало файла
# и данные пишутся поверх существующих
with open('text.txt', 'r+', encoding='utf-8') as f:
    f.write('Machine')

# режим А - это режим на дозапись, курсор устанавливается в конец файла
# режим А позволяет создавать файл если такой файл не существует
with open('text.txt', 'a', encoding='utf-8') as f:
    f.write('Motocycle')
