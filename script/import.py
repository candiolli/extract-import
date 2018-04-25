import os

fl  = os.open('itau.csv', os.O_RDONLY)

print(fl)
os.close(fl)