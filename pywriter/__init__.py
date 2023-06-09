""" Pywriter
    Developed by Jesse Amarquaye.
    Copyright(C) 2023 Jesse Amarquaye.
"""

import sys
import time

def write(text, rate:float | None = 0.1):
    """Function to print output with typewriter effect
    
    >>> For instance:
        write(text="Hello world!", rate=1) 
        
        This will print all the elements of the string **Hello world!** one by one at the rate of 1 element per second.
    """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(rate)
    print()


def writer(text, rate:float | None = 0.1):
    """Function to print output with typewriter effect in reverse.
    
    >>> For instance:
        writer(text="Hello world!", rate=1) 
        
        This will print all the elements of the string **Hello world!** one by one at the rate of 1 element per second in the reverse order.
        This time it will print **!dlrow olleH** instead.
    """

    reversed_text = text[::-1] # Reverse the text
    for char in reversed_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(rate)
    print()


def typewriter(text, new, rate: float | None = 0.1, idx=None):
    """Function to print output with typewriter effect.
       Deletes some part of the text to some index and prints another text to replace the previous text.
    
    >>> For instance:
        typewriter(text="Hello world!", new="Pythonista", idx=6, rate=1) 
        
        This will print all the elements of the string **Hello world!** one by one at the rate of 1 element per second.
        Delete parts of **Hello world** till it reaches the index 6 then prints the value of new in the same typewriter effect.
   """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(rate)
    if idx is not None:
        deleted_text = text[idx:]
        for i in range(len(text)-1, idx-1, -1):
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(rate)
        for char in new:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(rate)
    print()
