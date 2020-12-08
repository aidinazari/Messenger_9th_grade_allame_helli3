
with open('example.csv','rb') as example_file:
    data=example_file.readlines()
    k=open('binfile3.bin','wb')
    k.writelines(data)
    k.close()
