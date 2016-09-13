#!/usr/bin/env python
# -*- coding: utf-8 -*-

DIGITS = 16

groups = (
    '000',
    '111',
    '222',
    '333',
    '444',
    '555',
    '666',
    '777',
    '888',
    '999',
)

if __name__ == '__main__':
    with open('nummern-' + str(DIGITS) + 'stellig.txt', 'w') as f:
        for i in range(10 ** DIGITS):
            number = str(i)
            
            if len(number) < DIGITS:
                tmplen = DIGITS - len(number)
                zeros = '0' * tmplen
                number = zeros + number
                
            #f.write(number + '\n')
            
            has_group = False
            for group in groups:
                if group in number:
                    has_group = True
                    break
                
            if not has_group:
                f.write(number + '\n')
            else:
                has_group = False
