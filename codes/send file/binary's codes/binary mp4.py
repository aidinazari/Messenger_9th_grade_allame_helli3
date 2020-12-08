
with open('tree.mp4','rb') as movie:
    data=movie.readlines()
    k=open('binfile2.bin','wb')
    k.writelines(data)
    k.close
