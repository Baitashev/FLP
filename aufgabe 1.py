def find_longest_word_by_delimiter(sentence, delimiter):
    words = sentence.split(delimiter)  # Разделяем строку на слова
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# Пример использования
sentence = input("Введите строку: ")
delimiter = ";"  # Используем точку с запятой как разделитель
longest_word = find_longest_word_by_delimiter(sentence, delimiter)

if longest_word:
    print("Самое длинное слово:", longest_word)
else:
    print("Строка пуста.")
