# coding=utf-8
from decimal import *
from hashlib import sha224
import re

f = open("0.txt")

getcontext().prec = 30
current = Decimal(0.02000000000000000000000000001)+1

try:
    m = Decimal(0.00000000000000000000000000001)
    i = 0
    while current < Decimal(0.06666666666666666666666666667)+1:
        f.write(str(current).replace(r"1.", "0.")+" => "+sha224(str(current).replace(r"1.", "0.")).hexdigest()+"\n")
        current += m
        i += 1
        if re.match(r"000$", str(current)):
            f.flush()
            print "Обработано "+str(i)+"k;"
finally:
    f.close()
