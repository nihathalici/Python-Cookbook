# Exer-02-Writing-Functions-That-Only-Accept-Keyword-Arguments

def recv(maxsize, *, block):
    'Receives a message'
    pass

# print(recv(1024, True))  # TypeError
print(recv(1024, block=True))

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))

#msg = recv(1024, False)
#print(msg)
msg = recv(1024, block=False)
print(msg)

print(help(recv))

