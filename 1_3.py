import os
dir = '/root/folder'
onlyfiles = next(os.walk(dir))
print len(onlyfiles)
