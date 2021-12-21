from urllib.request import urlopen

f = urlopen('https://www.youtube.com/watch?v=Qn3nfR3Tujc')
print(type(f))
print(f.headers)
print(f.read())