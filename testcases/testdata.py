import subprocess

import time

#subprocess.call(['python','/home/nrv/PycharmProjects/publiclink/newDeamon.py'])

proc = subprocess.Popen(['python','/home/nrv/PycharmProjects/publiclink/newDeamon.py'])
print proc.pid

for k in range(0,150):
    print k
    time.sleep(1)