import os


for i in range(2,100):
    name = "./K-MOOC/RMaURA/K-MOOC_RMaURA6-3 ({}).jpg".format(i)
    new_name = "./K-MOOC/RMaURA/K-MOOC_RMaURA6-3_({}).jpg".format(i)
    os.rename(name, new_name)