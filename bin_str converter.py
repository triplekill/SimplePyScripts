#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def bin_str_to_text(bin_str):
    all_text = ''

    for bin_word in text.split():
        n = int(bin_word, base=2)
        all_text += chr(n)

    return all_text


def text_to_bin_str(text):
    bin_words = list()

    for c in text:
        bin_words.append(
            bin(ord(c)).replace('0b', '').rjust(8, '0')
        )

    return ' '.join(bin_words)


text = ("01011001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01101101 01101111 01110010 01100101 "
        "00100000 01110100 01101000 01100001 01101110 00100000 01101010 01110101 01110011 01110100 00100000 01100001 "
        "01101110 00100000 01100001 01101110 01101001 01101101 01100001 01101100 00101110 00001101 00001010 01010101 "
        "01110011 01100101 00100000 01110100 01101000 01100101 00100000 01110011 01101111 01110101 01101100 00100000 "
        "01111001 01101111 01110101 00100111 01110110 01100101 00100000 01100010 01100101 01100101 01101110 00100000 "
        "01100111 01101001 01110110 01100101 01101110 00101110 00001101 00001010 01000001 01101110 01100100 00100000 "
        "01100010 01100101 00100000 01110010 01100101 01110011 01110000 01101111 01101110 01110011 01101001 01100010 "
        "01101100 01100101 00100000 01100110 01101111 01110010 00100000 01111001 01101111 01110101 01110010 00100000 "
        "01100001 01100011 01110100 01101001 01101111 01101110 01110011 00101110")
print(bin_str_to_text(text))

text = "You are more than just an animal."
print(text_to_bin_str(text))