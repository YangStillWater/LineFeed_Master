__author__ = 'Peng'


def count_word(text):
    wlist = text.split()
    return len(wlist)


def line_feed(text, width=40, whitespace=' '):
    rtn = ''
    while len(text) > width:
        rtn += text[:width]
        text = text[width:]
        if text[0] not in whitespace:
            i = 1
            while text[i] not in whitespace:
                i += 1
            rtn += text[:i]
            text = text[i:]
        rtn += '\n'
    rtn += text
    return rtn
