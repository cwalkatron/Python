#!/usr/bin/env python

from random import choice

words = "salt fat anchor longshoreman sail mustache saw beard churn weight " \
        "lamp wood whale axe pepper basil tamarind thyme cinnamon consumption " \
        "burgandy porch brew pickle candle toad spoon fork knife lamb " \
        "oil kettle compass ox"

words = words.split()

first_word = choice(words)
second_word = first_word
while first_word == second_word:
    second_word = choice(words)

print "{0} & {1}".format(first_word, second_word)
