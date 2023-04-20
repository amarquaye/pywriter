import time


def write(text, rate:float | None = 0.01):
    """Function to print output with typewriter effect
    
    >>> For instance:
        write(text="Hello world!", rate=1) 
        
        This will print all the elements of the string "Hello world!" one by one at the rate of 1 element per second
    """

    for i in range(len(text)):
        print(text[i], end="")
        time.sleep(rate)