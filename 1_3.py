import os
dir = '/dev'
onlyfiles = next(os.walk(dir))
print len(onlyfiles)
