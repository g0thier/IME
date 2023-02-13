import os 
import time 
from datetime import datetime
import re


os.system('docker')
time.sleep(2)

now = str( datetime.today().strftime("%y%m%d%H%M%S") )
os.system(f'docker build . -t applicationdocker{now}')
os.system(f'docker run -p 8080:8080 -e PORT=8080 applicationdocker{now}')