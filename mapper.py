#!/usr/bin/env python

import sys
import ast
for line in sys.stdin:
        line = line.strip()
        words=line.split('\t')
        data = ast.literal_eval(words[04])
        try:
                a = data["subjects"]
        except KeyError:
                a = ""
                pass
        for b in a:
                print "%s\t\t%s" %(b,1)
