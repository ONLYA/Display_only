import os
import sys

print("Starting...")
try:
        output = os.popen("python {}".format(sys.argv[0]))
except (BrokenPipeError, IOError):
        print("Exiting...", file = sys.stderr)
print("*", file=sys.stderr)
sys.stderr.close()
