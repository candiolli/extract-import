import os

fl  = os.open('/Users/macsilas/git/extract-import/script/itau.csv', os.O_RDONLY)

print(fl.readline(1))

os.close(fl)