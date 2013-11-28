'''
Created on Aug 14, 2013

@author: eric.huang
'''

li = [{'a':1, 'c':3, 'd':2},{'a':2, 'c':2, 'b':4}]
li2 = [{'a':1, 'c':3, 'd':2},{'a':2, 'c':2, 'b':4}]

li.sort()
print li
#TODO: a
li2.sort(cmp=None, key=lambda x: x['c'], reverse=False)
print li2