_input = "http://www.naver.com"
_input = _input.split('.')
text = list(_input)
password = text[1][:3]+str(len(text[1]))+str(text[1].count('e'))+"!"

print(password)