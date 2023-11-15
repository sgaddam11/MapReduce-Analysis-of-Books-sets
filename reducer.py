#!/usr/bin/env python

from operator import itemgetter
import sys

#initialing the variables
word = None
cur_count = 0
cur_word = None
max_sub = 0
max_sub_name = None
min_sub = 1
min_sub_name = None
list = []
for line in sys.stdin:
        #stripping the whitespaces
        line=line.strip()
        #spliting the line to word,count
        try:
                word,count = line.split('\t\t')
        except ValueError:
                pass
        #converting count variable from string to int
        try:
          count = int(count)
        except ValueError:
          continue
        #AS mapreduce framework sorts the output of mapper based on key we are going to use it in counting
        if cur_word == word:
                cur_count += count
        else:
          if cur_word:
                if max_sub < cur_count:
                        max_sub_name = cur_word
                        max_sub = cur_count
                if min_sub >= cur_count:
                        min_sub_name = cur_word
                        min_sub = cur_count
                print "%s\t%s" %(cur_word,cur_count)
                list.append(cur_count)
          cur_count = count
          cur_word = word
if cur_word == word:
        if max_sub < cur_count:
                max_sub_name = cur_word
                max_sub = cur_count
        if min_sub > cur_count:
                min_sub_name = cur_word
                min_sub = cur_count
        print "%s\t%s" %(cur_word,cur_count)
        list.append(cur_count)
print "maximum_subject\t%s" %(max_sub_name)
print "minimum_subject\t%s" %(min_sub_name)
list.sort()
print "count_median\t%s"  %(list[len(list)/2])
print "count_average\t%s" %(sum(list)/len(list))
