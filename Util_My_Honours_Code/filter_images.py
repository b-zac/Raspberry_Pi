import os

path = "WIDER_val/images"

for subpath in os.listdir(path):
    print(path + "/" + subpath)
    directory = os.listdir(path + "/" + subpath)

    for i, picture in enumerate(directory):
        isValid = True
        with open('wider_face_val_bbx_gt.txt') as bbx:

            for j, line in enumerate(bbx):
                picturePath = subpath + "/" + picture + "\n"
                if line == picturePath:
                    #print("matches")
                    isValid = True
                    break
                else:
                    isValid = False

            if isValid == False:
                os.remove(path + "/" + subpath + "/"+ picture)
                #print("remove " + path + "/" + subpath + "/"+ jpg)