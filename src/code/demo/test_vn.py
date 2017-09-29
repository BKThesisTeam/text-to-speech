#!/usr/bin/python
# -*- coding: utf8 -*-
import nltk

cau = u'Tôi đi học'
print cau, len(cau)

for char in cau:
	print char

words = cau.split(" ")
print words

for i in words:
	print i, len(i)

tokens = nltk.pos_tag(words)
print tokens

print tokens.pop(0)[0]
print tokens.pop(0)[0]
print tokens.pop(0)[0]
	