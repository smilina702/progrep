print("Вариант 2")
with open("text1.txt", encoding = "utf -8-sig") as f:
    lines = f.readlines()
if len(lines) <= 1: 
    print("Недостаточно строк")
else:
    min_line = len(lines[0].replace("\n", "")) #убираем символ переноса в минимальной и максимальной строке
    max_line = len(lines[0].replace("\n", "")) 
    for line in lines:
        line = line.replace("\n", "") #убираем символ переноса 
        if len(line) >= max_line:
            max_line = len(line)
        if len(line) <= min_line and len(line) != 0: #минимальная строка должна содержать хотя бы один символ
            min_line = len(line)
    print('Самая короткая строка короче самой длинной в', round(max_line / min_line, 2), 'раз(а)')
    
