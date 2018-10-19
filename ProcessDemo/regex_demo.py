# coding=utf-8

import re
import doctest

class RegexDemo(object):

    '''
    tests
    >>> RegexDemo().is_valid_email('Someone@gmail.com')
    True
    >>> RegexDemo().is_valid_email('bill.gates@microsoft.com')
    True
    >>> RegexDemo().is_valid_email('bob#example.com')
    False
    >>> RegexDemo().is_valid_email('mr-bob@example.com')
    False

    >>> RegexDemo().name_of_email('<Tom Paris> tom@voyager.org')
    'Tom Paris'
    >>> RegexDemo().name_of_email('tom@voyager.org')
    'tom'
    '''
    def is_valid_email(self, addr):
        if re.match(r"^[\w\d_.]+@[\w\d]+(\.[\w\d]+)*\.[\w\d]{2,6}$", addr):
            return True
        else:
            return False

    def name_of_email(self, addr):
        subStr = re.split(r'@', addr)
        if re.match('\w+', subStr[0]):
            return subStr[0]
        else:
            return re.split(r'[\<\>]', subStr[0])[1]

if __name__ == '__main__':
    doctest.testmod()