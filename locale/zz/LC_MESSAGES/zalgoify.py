from zalgo_text import zalgo
import os 
import random

def random_unicode(length):
    # Create a list of unicode characters within the range 0000-D7FF
    random_unicodes = [] 
    for _ in range(0, length):
        c = chr(random.randrange(0x3300))
        if c!= '"' and c!="'" and c!="\n" and c!="\t" and c!="\r":#helps with translation file generation
            random_unicodes.append(c)
    return u"".join(random_unicodes)

my_random_unicode_str = random_unicode(length=512)
my_random_utf_8_str = my_random_unicode_str.encode('utf-8')

d = os.path.dirname(os.path.realpath(__file__))
newlines = []
with open(d+'/django.po') as f:
    l = f.readline()
    while l:
        if l[0:5]=="msgid":
            b = l.find('"')+1
            e = l.rfind('"')
            if b+1<e:
                newlines.append(l)
                l = f.readline()
                l = 'msgstr "'+zalgo.zalgo().zalgofy(random_unicode(e-b))+'"\n'
        newlines.append(l)
        l = f.readline()
    newlines.append(l)


with open(d+"/django_new.po", "a+") as document1:
        document1.writelines(newlines)

os.replace(d+"/django_new.po", d+"/django.po")