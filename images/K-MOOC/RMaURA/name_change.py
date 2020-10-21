import os

print(os.listdir("./"))

for i in (os.listdir("./")):
    new_name = i[:]
    print(i[i.find(" ")])
    if(i.find(" ") > 0):
        new_name = new_name.replace(" ","_")
        os.rename(i,new_name)
# for i in range(2,18):
#     name = "Mask_RCNN_tutorial ({})".format(i)
#     new_name = "Mask_RCNN_tutorial_({})".format(i)
#     os.rename(name, new_name)