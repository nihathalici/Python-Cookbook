# Exer-01-Reading-and-Writing-Text-Data


with open('somefile.txt', 'rt') as f:
    data = f.read()
    print(data)
###

with open("somefile.txt", "rt") as f:
    for line in f:
        print(line)
###


txt_to_wr1 = "When in the chronicle of wasted time\n"
txt_to_wr2 = "I see descriptions of the fairest wights,"

with open("somefile2.txt", "wt") as f:
    f.write(txt_to_wr1)
    f.write(txt_to_wr2)

###    


with open("somefile.txt", "wt") as f:
    print(line1, file=f)
    print(line2, file=f)
    
###



f = open("somefile.txt", "rt")
data = f.read()
f.close()

###

with open("somefile.txt", "rt") as f:
    for line in f:
        print(line)

###

# Newline translation enabled (the default)
f = open("hello.txt", "rt")
f.read()
# 'hello world!\n'

# Newline translation disabled
g = open("hello.txt", "rt", newline='')
g-read()
# 'hello world!\r\n'

###

f = open('sample.txt', 'rt', encoding='ascii')
f.read()  # UnicodeDecodeError

# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()  # 'Spicy Jalape?o!'

# Ignore bad chars entirely
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read()  # 'Spicy Jalapeo!'
