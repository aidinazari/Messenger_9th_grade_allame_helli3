
f = open('parrot.jpg', 'rb')
data=f.readlines()
k=open('binfile.bin','wb')
k.writelines(data)
k.close()

from PIL import Image
tasvir=Image.open('binfile.bin')
tasvir.show()



