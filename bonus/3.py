glas = 'AaEeIiOoUuYy'
word = str(input("add word or phrase:"))
if word == '':
    print("no word((((")
else:
    for char in glas:
        word = word.replace(char, '.'+char)
        letter = word.split(".")
        letters = ''.join(map(str, letter[1:]))
    print(letters+letter[0]+'ay')

##
##    words = word. replace(" ", "|")
##    words = words.split("|")
##    print(words)
##    for words in word:
##        for char in glas:
##            words = words.replace(char, '.'+char)
##            letter = words.split(".")
##            letters = ''.join(map(str, letter[1:]))
##        words = letters+letter[0]+'ay'
##        print(words)

        
        
 #все еще пытаюсь понять, почему так не срабатывает для фразы
