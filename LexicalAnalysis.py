# -*- coding: utf-8 -*-
__author__ = 'simon'


# 保留字表
WORD = {"DO", "BEGIN", "ELSE", "END", "IF", "THEN", "VAR", "WHILE","CONST","PROCEDURE"}


SYM = {}
NUM = {}
ID = {}
def next_alpha( line ):
    for ch in line:
        yield ch


def identify(id):
    # print id

    if id in WORD:
        SYM[id] = id+"SYM"
    elif id.isdigit():
        SYM[id] = "NUMBER"
        NUM[id] = id
    elif id[0].isalpha():
        SYM[id] = "IDENT"
        ID[id] = id
    else:
        SYM[id] = "SYMBOL"


def error(msg):
    raise BaseException(msg)


def getsym(text):

    for line in text:
        # print line
        gen = next_alpha(line)

        ch = next(gen)
        while True:
            if ch == " ":
                ch = next(gen)
            try:
                if ch.isalpha():
                    k = 0
                    a = []
                    while k < 10 and (ch.isalpha() or ch.isdigit()):
                        a.append(ch)
                        k += 1
                        ch = next(gen)
                    id = "".join(a)
                    identify(id)

                elif ch.isdigit():
                    a = []
                    while ch.isdigit():
                        a.append(ch)
                        ch = next(gen)
                    # deal with exception
                    if ch.isalpha():
                        error("syntax error")
                    s = "".join(a)
                    identify(s)
                elif ch != " ":
                    a = []
                    while ch != ' ' and not ch.isalpha() and not ch.isdigit():
                        a.append(ch)
                        ch = next(gen)
                    s = "".join(a)
                    identify(s)

            except StopIteration:
                break



if __name__ == "__main__":
    with open("test.in","r") as f:
        line = f.readlines()
        getsym(line)

    print SYM
    print NUM
    print ID