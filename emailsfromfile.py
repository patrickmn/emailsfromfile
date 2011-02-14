#!/usr/bin/env python
'''
  emailsfromfile.py -- Get all unique email addresses from a file

  by Patrick Mylund Nielsen
  http://patrickmylund.com/projects/emailsfromfile/

  License: WTFPL (http://sam.zoy.org/wtfpl/)
'''

import sys
import os
import re
import codecs

__version__ = '1.1'

# Regular expression matching according to RFC 2822 (http://tools.ietf.org/html/rfc2822)
rfc2822_regex = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
email_expr = re.compile(rfc2822_regex, re.IGNORECASE)

def isEmail(string):
    return email_expr.match(string)

def main(filename, separator='\n', encoding=None):
    results = set()
    if not os.path.isfile(filename):
        print("%s is not a file." % filename)
        return
    f = codecs.open(filename, 'rb', encoding)
    for line in f:
        results.update(email_expr.findall(line))
    if separator == 'space':
        separator = ' '
    elif separator == 'newline':
        separator = '\n'
    print(separator.join(results))

if __name__ == '__main__':
    args = len(sys.argv) - 1
    if 0 < args < 4:
        main(*sys.argv[1:])
    else:
        print("Usage: python %s <filename> [separator] [encoding]" % sys.argv[0])
        print("The default separator is a newline. To separate by space, literally enter 'space' as the separator.")
