import sys
import os
import time
import random

filename = sys.argv[2] if len(sys.argv) > 2 else os.environ.get('filename', 'world')


time.sleep(random.randrange(1,3))
print(f"Processing file: {filename}")

