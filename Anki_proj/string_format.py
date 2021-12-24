from string import ascii_letters
from automatic_search import AutomaticSearch


class Format4Anki:
    word_classes = ['명사', '대명사', '동사', '부사', '형용사', '전치사', '접속사', '감탄사']
    other_lst = ['문형', '유의어', '반의어', '참고어']
    about_pronounce = ['발음듣기', '반복듣기']
    broken_char_in_utf8 = {'∙': '/', 'ˌ': ', ', 'ˈ': '\''}

    def __init__(self, lst) -> None:
        self.word_lst = lst[0].split('\n')
        self.pronounce_lst = lst[1].split('\n')
        self.meaning_lst = lst[2].split('\n')
        self.ex_sentence_lst = lst[3].split('\n')
        self.tag_lst = []

    def format_pronounce(self):
        for i in range(len(self.pronounce_lst)):
            if self.pronounce_lst[i].startswith('발음 '):
                self.pronounce_lst[i] = self.pronounce_lst[i][3:]

        string = '\n'.join(self.pronounce_lst)
        return string

    def format_meaning(self):
        for i in range(len(self.meaning_lst)):
            if self.meaning_lst[i - 1] in self.other_lst:
                for obj in self.other_lst:
                    if self.meaning_lst[i - 1] == obj:
                        self.meaning_lst[i] = f'{obj}: {self.meaning_lst[i]}'
                        break
                self.meaning_lst[i - 1] = ''
            for word_class in self.word_classes:
                if (word_class in self.meaning_lst[i]) and (self.meaning_lst[i + 1].startswith('1. ')) and (i != 0):
                    self.meaning_lst[i] = '\n' + self.meaning_lst[i]
                    break
            if (self.meaning_lst[i][1:3] == '. '):
                for char in ascii_letters:
                    if char in self.meaning_lst[i + 1]:
                        break
                else:
                    self.meaning_lst[i] = f'{self.meaning_lst[i]}//{self.meaning_lst[i + 1]}'
                    self.meaning_lst[i + 1] = ''

        string = ''
        for i in range(len(self.meaning_lst)):
            if self.meaning_lst[i]:
                if i == len(self.meaning_lst) - 1:
                    string += self.meaning_lst[i]
                string += (self.meaning_lst[i] + '\n')

        return string

    def format_ex_sentence(self):
        for i in range(len(self.ex_sentence_lst)):
            if self.ex_sentence_lst[i] in self.about_pronounce:
                self.ex_sentence_lst[i] = ''
            if i == len(self.ex_sentence_lst) - 1:
                self.ex_sentence_lst[i] = ''

        string = '\n'.join(self.ex_sentence_lst)
        return string

    def format_tag(self):
        for i in range(len(self.meaning_lst)):
            for word_class in self.word_classes:
                if (word_class in self.meaning_lst[i]) and (self.meaning_lst[i + 1].startswith('1. ')):
                    self.tag_lst.append(f'#{word_class}')
                    break

        if ' ' in self.word_lst[0]:
            self.tag_lst.append('#숙어')

        string = ''.join(self.tag_lst)
        return string

    def replace_broken_char(self):
        exam_lst = [self.word_lst, self.pronounce_lst,
                    self.meaning_lst, self.ex_sentence_lst]
        for obj in exam_lst:
            for i in range(len(obj)):
                for char in self.broken_char_in_utf8.keys():
                    if char in obj[i]:
                        obj[i] = obj[i].replace(
                            char, self.broken_char_in_utf8[char])


if __name__ == '__main__':
    word = 'a lot of'
    auto_search = AutomaticSearch()
    auto_search.set_word(word)
    word_lst = auto_search.get_word()

    formatter = Format4Anki(word_lst)
    formatter.replace_broken_char()

    print(word)
    print(formatter.format_pronounce())
    print(formatter.format_meaning())
    print(formatter.format_tag())
