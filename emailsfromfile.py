#!/usr/bin/env python
'''
  emailsfromfile.py -- Get all unique email addresses from a file

  by Patrick Mylund Nielsen
  http://patrickmylund.com/projects/emailsfromfile/

  License: WTFPL (http://sam.zoy.org/wtfpl/)
'''

__version__ = '1.1'

import sys
import os
import re
import codecs

# Regular expression matching according to RFC 2822 (http://tools.ietf.org/html/rfc2822)
rfc2822_re = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
email_prog = re.compile(rfc2822_re, re.IGNORECASE)

def isEmailAddress(string):
    return email_prog.match(string)

def main(filename, separator='\n', encoding=None):
    separator_replace = {
        'space': ' ',
        'newline': '\n',
    }
    if not os.path.isfile(filename):
        raise IOError("%s is not a file." % filename)
    results = set()
    with codecs.open(filename, 'rb', encoding) as f:
        for line in f:
            results.update(email_prog.findall(line))
    for k, v in separator_replace.iteritems():
        separator = separator.replace(k, v)
    print(separator.join(results))

if __name__ == '__main__':
    args = len(sys.argv) - 1
    if 0 < args < 4:
        main(*sys.argv[1:])
    else:
        print("Usage: python %s <filename> [separator] [encoding]" % sys.argv[0])
        print("The default separator is a newline. To separate by space, literally enter 'space' as the separator.")
