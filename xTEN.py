import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import xTEN
elif bit=='32bit':
    import xTEN32
