#!/usr/bin/python3
def multiple_returns(sentence):
    i = sentence[0]
    if len(sentence) == 0:
        i = None
        return (0, None)
    else:
        return (len(sentence), sentence[0])
