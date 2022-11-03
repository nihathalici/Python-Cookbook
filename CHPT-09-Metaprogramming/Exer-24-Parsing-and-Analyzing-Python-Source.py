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

