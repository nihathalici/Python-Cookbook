# Exer-06-Executing-an-External-Command-and-Getting-Its-Output

import subprocess

out_bytes = subprocess.check_output(['netstat', '-a'])

out_text = out_bytes.decode('utf-8')

###

try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode

###

out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], stderr=subprocess.STDOUT)

###

try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], timeout=5)
except subprocess.TimeoutExpired as e:

###

out_bytes = subprocess.check_output('grep python | wc > out', shell=True)

###

import subprocess

# Some text to send
text = b"""
hello world
this is a test
goodbye
"""

# Launch a command with pipes
p = subprocess.Popen(['wc'],
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')


