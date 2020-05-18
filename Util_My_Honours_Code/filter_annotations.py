
with open('somefile.txt', 'a') as the_file:
    with open("wider_face_train_bbx_gt.txt") as fp:

            currentFileName = ""

            nextFileName = 0
            nextBoundry = 1
            boundryStart = 0

            isValidBoundry = False
            wroteFileName = False

            for i, line in enumerate(fp):
                noBoundries = 0
                if i == nextFileName:
                    #   Get file name
                    currentFileName = line
                    wroteFileName = False
                if i == nextBoundry:
                    #   Process boundries
                    noBoundries = int(line)

                    if noBoundries == 0:
                        noBoundries = 1
                        isValidBoundry = False
                    elif noBoundries == 1:
                        isValidBoundry = True
                    else:
                        isValidBoundry = False
                    nextBoundry = i+2+noBoundries
                    nextFileName = i+1+noBoundries

                    # if isValidBoundry:
                    #     the_file.write(currentFileName + "\n")
                    #     the_file.write(str(noBoundries) + "\n")
                if i+1< nextBoundry:
                    #   Write boundries

                    if isValidBoundry:
                        if wroteFileName == False:
                            the_file.write(currentFileName)
                            wroteFileName = True
                        the_file.write(line)



        