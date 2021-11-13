import random


class TextLoader:

    def loadtext(self, name):
        txt = open(name)
        textlist=txt.read().splitlines()
        print(len(textlist))
        return textlist[random.randrange(0, len(textlist))]

