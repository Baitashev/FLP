def count_words(sentence):
    words = sentence.split()  # Разделяем строку на слова
    return len(words)

# Пример использования
sentence = input("Введите предложение: ")

word_count = count_words(sentence)
print("Количество слов в предложении:", word_count)
        