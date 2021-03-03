import platform
from pathlib import Path
s = platform.system()
if s == 'Linux':
    bk = '/'
elif s == 'Windows':
    bk = '\\'
    
    



path = Path(__file__).parent.absolute()
path = str(path)

start_file = path + bk

