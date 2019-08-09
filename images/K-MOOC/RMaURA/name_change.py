import os


for i in range(2,18):
    name = "Mask_RCNN_tutorial ({})".format(i)
    new_name = "Mask_RCNN_tutorial_({})".format(i)
    os.rename(name, new_name)