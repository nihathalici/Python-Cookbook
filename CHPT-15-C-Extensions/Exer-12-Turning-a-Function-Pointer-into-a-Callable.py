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

###

from llvm.core import Module, Function, Type, Builder

mod = Module.new("example")
f = Function.new(
    mod, Type.function(Type.double(), [Type.double(), Type.double()], False), "foo"
)
block = f.append_basic_block("entry")
builder = Builder.new(block)
x2 = builder.fmul(f.args[0], f.args[0])
y2 = builder.fmul(f.args[1], f.args[1])
r = builder.fadd(x2, y2)
builder.ret(r)  # <llvm.core.Instruction object at...

from llvm.ee import ExecutionEngine

engine = ExecutionEngine.new(mod)
ptr = engine.get_pointer_to_function(f)
foo = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(ptr)

# Call the resulting function
foo(2, 3)  # 13.0
foo(4, 5)  # 41.0
foo(1, 2)  # 5.0
