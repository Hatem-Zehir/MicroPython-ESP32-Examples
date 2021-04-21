"""
    ASCII table

    Prints out byte values in all possible formats:
    - as raw binary values
    - as ASCII-encoded decimal, hex, octal, and binary values

    For more on ASCII, see http://www.asciitable.com and http://en.wikipedia.org/wiki/ASCII

    The circuit: No external hardware needed.
"""

# prints title with ending line break
print("ASCII Table ~ Character Map")

# first visible ASCIIcharacter '!' is number 33:
thisByte = 33

while True:
    print(chr(thisByte), ", dec: ", thisByte, ", hex: ", hex(thisByte), ", oct: ", oct(thisByte), ", bin: ", bin(thisByte))
    # if printed last visible character '~' or 126, stop:
    if (thisByte == 126):
    # This loop loops forever and does nothing
        while True:
            pass
    thisByte = thisByte + 1
