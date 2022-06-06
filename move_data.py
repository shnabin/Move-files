import os
import shutil
import time
  
source = 'C:\\Users\\Administrator\\Documents\\Alt\\'
destination = 'C:\\Users\\Administrator\\Documents\\old_Alt\\'
  
allfiles = os.listdir(source)

for f in allfiles:
    shutil.move(source + f, destination + f)

