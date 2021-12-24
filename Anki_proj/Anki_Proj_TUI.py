# -*- coding: utf-8 -*-

from string import ascii_letters
import time
import os
from automatic_search import AutomaticSearch
from string_format import Format4Anki


def file_write(string_lst):
    file_name = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}-Engword.txt'
    file_path = 'C:\\Users\\jeony\\OneDrive\\바탕 화면'

    if not os.path.isfile(f'{file_path}\\{file_name}'):
        with open(f'{file_path}\\{file_name}', 'wt', encoding='utf-8') as f:
            for i in range(len(string_lst)):
                if i == len(string_lst) - 1:
                    f.write(f'"{string_lst[i]}"\n')
                else:
                    f.write(f'"{string_lst[i]}"\t')
                print(string_lst[i])
            f.close()
    else:
        with open(f'{file_path}\\{file_name}', 'at', encoding='utf-8') as f:
            for i in range(len(string_lst)):
                if i == len(string_lst) - 1:
                    f.write(f'"{string_lst[i]}"\n')
                else:
                    f.write(f'"{string_lst[i]}"\t')
                print(string_lst[i])
            f.close()


program_start = True
while program_start:
    reset = False

    print("""Enter the English word
    (If you want to quit then pls enter the \'quit\'.)
    -> """, end='')
    input_word = input().lower().strip()

    if input_word == "quit":
        program_start = False
        break
    for char in input_word:
        if not char in ascii_letters:
            print("pls enter the English word")
            reset = True
            break

    if reset:
        continue

    ChromeDriver = AutomaticSearch()
    ChromeDriver.set_word(input_word)
    word_lst = ChromeDriver.get_word()

    formatter = Format4Anki(word_lst)
    formatter.replace_broken_char()
    string_lst = [f'{input_word}\n{formatter.format_pronounce()}',
                  formatter.format_meaning(), formatter.format_tag()]

    file_write(string_lst)
