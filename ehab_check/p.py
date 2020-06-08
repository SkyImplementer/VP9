import struct
import binascii



x=""
f = open("headerhis1", "rb")
c=0
try:
    byte = f.read(1)
    while byte != "":
        binary_string = (format(ord(byte),'08b'))
        x+= binary_string         

	byte = f.read(1)
finally:
    f.close()


print x[120:124]
