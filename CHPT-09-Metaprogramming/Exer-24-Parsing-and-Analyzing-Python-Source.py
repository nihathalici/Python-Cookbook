# Exer-24-Parsing-and-Analyzing-Python-Source

x = 42
#print(eval('2 + 3*4 + x'))
#print(exec('for i in range(10): print(i)'))

###

import ast

ex = ast.parse('2 + 3*4 + x', mode='eval')
#print(ex)
#print(ast.dump(ex))
top = ast.parse('for i in range(10): print(i)', mode='exec')
#print(top)
print(ast.dump(top))

###
import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)

# Sample usage
if __name__ == '__main__':
    # Some Python code
    code '''
for i in range(10):
    print(i)
del i
'''

# Parse into an AST
top = ast.parse(code, mode='exec')

# Feed the AST to analyze name usage
c = CodeAnalyzer()
c.visit(top)
print('Loaded:', c.loaded)
print('Stored:', c.stored)
print('Deleted:', c.deleted)

###

print(exec(compile(top, '<stdin>', 'exec')))

###

import ast
import inspect

class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names
    
    def visit_FunctionDef(self, node):
        code = '__globals = globals()\n'
        code += '\n'.join("{} = __globals['{0}']".format(name)
                           for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')

        node.body[:0] = code_ast.body

        self.func = node
    
    def lower_names(*namelist):
        def lower(func):
            srclines = inspect.getsource(func).splitlines()
            for n, line in enumerate(srclines):
                if '@lower_names' in line:
                    break
            
            src = '\n'.join(srclines[n+1:])

            if src.startswith((' ', '\t')):
                src = 'if 1:\n' + src
            top = ast.parse(src, mode='exec')

            cl = NameLower(namelist)
            cl.visit(top)

            temp = {}
            exec(compile(top, '', 'exec'), temp, temp)

            func.__code__ = temp[func.__name__].__code__
            return func
        return lower

INCR = 1

@lower_names('INCR')
def countdown(n):
    while n > 0:
        n -= INCR

def countdown(n):
    __globals = globals()
    INCR = __globals['INCR']
    while n > 0:
        n -= INCR
        
