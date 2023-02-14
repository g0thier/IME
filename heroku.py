import os 
import time 
from datetime import datetime
import re

os.system('docker')
time.sleep(2)

print('')
now = str(datetime.today().strftime("%y%m%d%H%M%S"))
name_input = input("A name for heroku app (only letters):").lower()
name = f'{name_input}{now}'
print('')

now = str(datetime.today().strftime("%y%m%d%H%M%S"))

send_name = f'{name}{now}'
send_name = send_name[:30]

os.system(f'docker build . -t {send_name}')

os.system(f'docker run -p 8080:8080 -e PORT=8080 applicationdocker{now}')

'''
os.system('heroku login')
time.sleep(10)
os.system("heroku container:login")

# vérifier si l'application existe déjà
app_exist = os.system(f"heroku apps:info {send_name}")
if app_exist == 0:
    print("Application already exists.")
    exit(1)

# création de l'application Heroku
os.system(f"heroku create {send_name}")
os.system(f"heroku container:push web -a {send_name}")
os.system(f"heroku container:release web -a {send_name}")
os.system(f"heroku open -a {send_name}")
'''