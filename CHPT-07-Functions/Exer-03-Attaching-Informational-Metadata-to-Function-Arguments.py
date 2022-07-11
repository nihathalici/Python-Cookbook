# Exer-03-Attaching-Informational-Metadata-to-Function-Arguments

def add(x:int, y:int) -> int:
    return x + y

print(help(add))

print(add.__annotations__)
