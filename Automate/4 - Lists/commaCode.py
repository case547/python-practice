spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(spam):
    c = ''
    for i in range(len(spam)):
        if i == len(spam) - 1:
            c += 'and ' + spam[i]
        else:
            c += spam[i] + ', '
    print(c)

commaCode(spam)