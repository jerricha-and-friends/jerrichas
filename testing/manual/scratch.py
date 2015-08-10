# Scartch file for figuring out face scale conversion
from ctypes import c_char, c_float, c_int, c_byte

def int_convert(x, y, z):
    x, y, z = float(x), float(y), float(z)
    # return c_char(c_float(z) * 100) << 16 | c_char(c_float(y) * 100) << 8 | c_char(c_float(x) * 100)
    # return c_char(z * 100) << 16 | c_char(y * 100) << 8 | c_char(c_float(x) * 100)
    return int(z * 100) << 16 | int(y * 100) << 8 | int(x * 100)


# Nose scales from testing/data/analysis/huge.save.csv
x = "0.110001"
y = "-0.700002"
z = "0.089999"

assert int_convert(x, y, z) == 640523  # Value from the ParagonChatDB
