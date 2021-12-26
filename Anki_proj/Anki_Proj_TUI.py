# -*- coding: utf-8 -*-

from string import ascii_letters
import string
import time
import os
from automatic_search import AutomaticSearch
from string_format import Format4Anki


class AnkiTui:
    def __init__(self) -> None:
        self.input_words = []
        self.file_name = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}-Engword.txt'
        self.file_path = 'C:\\Users\\jeony\\OneDrive\\바탕 화면'
        self.temp_lst = []
        
    def file_write(self, string_lst):
        if not os.path.isfile(f'{self.file_path}\\{self.file_name}'):
            with open(f'{self.file_path}\\{self.file_name}', 'wt', encoding='utf-8') as f:
                for i in range(len(string_lst)):
                    if i == len(string_lst) - 1:
                        f.write(f'"{string_lst[i]}"\n')
                    else:
                        f.write(f'"{string_lst[i]}"\t')
                    print(string_lst[i])
                    print()
                f.close()
        else:
            with open(f'{self.file_path}\\{self.file_name}', 'at', encoding='utf-8') as f:
                for i in range(len(string_lst)):
                    if i == len(string_lst) - 1:
                        f.write(f'"{string_lst[i]}"\n')
                    else:
                        f.write(f'"{string_lst[i]}"\t')
                    print(string_lst[i])
                    print()
                f.close()

    def display(self):
        program_start = True
        while program_start:
            reset = False

            intro_msg = """Enter the English word
            (If you want to quit then pls enter the \'quit\'.)
            -> """
            print(intro_msg, end='')
            input_word = input().lower().strip()

            for char in input_word:
                if (not char in ascii_letters) and not (char in [' ', '-']):
                    print("pls enter the English word")
                    reset = True
                    break

            if reset:
                continue

            if input_word == "quit":
                program_start = False

                self.main()
                
                if self.temp_lst:
                    print('You should re-do about these ones')
                    for obj in self.temp_lst:
                        print(obj, end = ', ')

            self.input_words.append(input_word)
    
    def main(self):
        for word in self.input_words[:]:
            ChromeDriver = AutomaticSearch()
            ChromeDriver.set_word(word)
            word_lst = ChromeDriver.get_word()

            if type(word_lst) == str:
                self.temp_lst.append(word_lst)
            else:
                formatter = Format4Anki(word_lst)
                formatter.replace_broken_char()
                string_lst = [f'{word}\n{formatter.format_pronounce()}', formatter.format_meaning(), formatter.format_tag()]

                self.file_write(string_lst)
            
            self.input_words.remove(word)

if __name__ == '__main__':
    anki_tui = AnkiTui()
    anki_tui.display()