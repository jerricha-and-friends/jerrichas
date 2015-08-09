from ctypes import c_char

int_convert = lambda x, y, z: c_char(float(z) * 100) << 16 | c_char(float(y) * 100) << 8 | c_char(float(x) * 100)

# Nose scales
x = "0.110001"
y = "-0.700002"
z = "0.089999"

assert int_convert(x, y, z) == 640523
