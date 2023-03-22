# Exer-02-Terminating-a-Program-with-an-Error-Message

# raise SystemExit('It failed!')

import sys

sys.stderr.write("It failed!\n")
raise SystemExit(1)
