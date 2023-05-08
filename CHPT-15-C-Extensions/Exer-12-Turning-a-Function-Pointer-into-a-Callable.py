# Exer-12-Turning-a-Function-Pointer-into-a-Callable

import ctypes

lib = ctpes.cdll.LoadLibrary(None)
# Get the address of sin() from the C math library
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value

# Turn the address into a callable function
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
func  # <CFunctionType object at ...

# Call the resulting function
func(2)  # 0.9092974268256817
func(0)  # 0.0
