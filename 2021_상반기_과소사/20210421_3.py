peaches = """I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
I get my light right from the source, yeah (yeah, that's it)
And I see you (oh), the way I breathe you in (in)
It's the texture of your skin
I wanna wrap my arms around you, baby
Never let you go, oh
And I say, oh, there's nothing like your touch
It's the way you lift me up, yeah
And I'll be right here with you 'til the end
I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
I get my light right from the source, yeah (yeah, that's it)
You ain't sure yet, but I'm for ya
All I could want, all I can wish for
Nights alone that we miss more
And days we save as souvenirs
There's no time, I wanna make more time
And give you my whole life
I left my girl, I'm in my Mallorca
Hate to leave her, call it torture
Remember when I couldn't hold her
Left the baggage for Rimowa
I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
I get my light right from the source, yeah (yeah, that's it)
I get the feeling, so I'm sure (sure)
Hand in my hand because I'm yours
I can't, I can't pretend, I can't ignore you're right for me
Don't think you wanna know just where I've been, oh
Done bein' distracted
The one I need is right in my arms (oh)
Your kisses taste the sweetest with mine
And I'll be right here with you 'til end of time
I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
I get my light right from the source, yeah (yeah, that's it)
I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
(I get my light right from the source, yeah, yeah)
I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
I get my light right from the source, yeah (yeah, that's it)
I got my peaches out in Georgia (oh, yeah, shit)
I get my weed from California (that's that shit)
I took my chick up to the North, yeah (badass bitch)
I get my light right from the source, yeah (yeah, that's it)"""

alphabet = dict()

for s in peaches:
    if s.isalpha() == False:
        continue
    s = s.lower()
    if s not in alphabet:
        alphabet[s] = 1
    else:
        alphabet[s] += 1

# print(alphabet)

temp = []

for key, value in alphabet.items():
    temp.append((key,value))

another = sorted(temp)
# print(another)

# print(alphabet.get('a'))