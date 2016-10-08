#!usr/bin/env python2.7

import re
#import sys
#import os

#key = '8bff558'
#key = '677c3cccccccc'
key = '6b4508380'
file0='part-00000'

with open(file0) as f:
    lines = f.readlines()
   
    for line in lines:
        result = re.split(';',line)    
        #print result
        #print result[0]      
        keystr = result[0]
        #print keystr
       
        if key in keystr:
            #print keystr
            print result

''' split example
value = 'asd;2234;aw4'
result = re.split(';', value)
for element in result:
    print(element) 
'''


