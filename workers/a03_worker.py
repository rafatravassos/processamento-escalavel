import sys
import os
import time
import random

import redis

r = redis.Redis(host='172.17.0.2', port=6379, db=0)

# Start consuming messages

while True:
    queue_name, message = r.blpop('file_queue')
    time.sleep(random.randrange(1,3))
    print(str(message))




