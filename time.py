#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    result=""
    single_digits = ["zero", "one", "two", "three", 
                     "four", "five", "six", "seven", 
                     "eight", "nine"];
 
    two_digits = ["", "ten", "eleven", "twelve", 
                  "thirteen", "fourteen", "fifteen", 
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"];
 
    tens_multiple = ["", "", "twenty","thirty","fourty","fifty"];
    if(m==00):
        result+=str(single_digits[h])+" o' clock"
    elif(m<10):
        result+=str(single_digits[m])+" minute past "+str(single_digits[h])
    elif(m<15):
        result+=str(two_digits[m+1])+" minutes past "+str(single_digits[h])
    elif(m==15):
        result+="quarter past "+str(single_digits[h])
    elif(m<20):
        result+=str(two_digits[(m%10)+1])+" minutes to "+str(single_digits[h])
    elif(m==20):
        result+=str(tens_multiple[2])+" minutes to "+str(single_digits[h])
    elif(m<30):
        result+=str(tens_multiple[2])+" "+str(single_digits[m%10])+" minutes past "+str(single_digits[h])
    elif(m==30):
        result+="half past "+str(single_digits[h])  
    elif(m<40):
        result+=str(tens_multiple[2])+" "+str(single_digits[(40-m)])+" minutes to "+str(single_digits[h+1])
    elif(m<45):
        result+=str(two_digits[m-40+1])+" minutes to "+str(single_digits[h+1])
    elif(m==45):
        result+="quarter to "+str(single_digits[h+1])
    elif(m<=50):
        result+=str(two_digits[50-m+1])+" minutes to "+str(single_digits[h+1])
    elif(m<59):
        result+=str(single_digits[60-m])+" minutes to "+str(two_digits[2])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
