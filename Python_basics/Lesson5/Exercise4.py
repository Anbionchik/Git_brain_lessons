# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file_for_lesson4_eng", "r", encoding='utf-8') as f_read, open("file_for_lesson4_ru", "w", encoding='utf-8') as f_write:
    for line in f_read:
        word, number = line.split(" — ")
        word = translate_dict[word]
        new_line = ' — '.join([word, number])
        f_write.write(new_line)

