def find_word_in_sentence(sentence, word):
    words = sentence.split()  # Разделяем строку на слова

    if word in words:
        return True
    else:
        return False

# Пример использования
sentence = input("Введите строку: ")
word_to_find = input("Введите слово для поиска: ")

if find_word_in_sentence(sentence, word_to_find):
    print("Слово '{}' найдено в строке.".format(word_to_find))
else:
    print("Слово '{}' не найдено в строке.".format(word_to_find))
