#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)

    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]

    return (lenght, first)
