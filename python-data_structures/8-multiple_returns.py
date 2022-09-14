#!/usr/bin/python3
def multiple_returns(sentence):
    i = sentence[0]
    if sentence == '':
        i = None
    else:
        return (len(sentence), sentence[0])
