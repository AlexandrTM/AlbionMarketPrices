import numpy as np
import math
from glob import glob
from PIL import Image, ImageChops


def getImageDifference(image1, image2):
    difference = ImageChops.difference(image1, image2)
    return 100 - np.mean(np.array(difference))


def getDigitsFromImage(imagePath, alphabet, variantsOfSymbol, sampleWidth):
    image = Image.open(imagePath)
    width, height = image.size
    digitSimilarityValues = [0] * 4
    digitSimilarityKeys = [0] * 4
    localDigitSimilarity = [float(0)] * len(alphabet)
    digitsFromImage = str()

    for i in range(math.floor(width / sampleWidth)):
        for j in range(1):
            imageRegion = image.crop((i * sampleWidth - min(i, 2), 2, i * sampleWidth + 6, 9))
            for k in range(3):
                imageSubRegion = imageRegion.crop((0 + k, 0, sampleWidth + k, 7))
                for l in range(len(alphabet)):
                    localDigitSimilarity[l] = getImageDifference(imageSubRegion, alphabet[l])
                digitSimilarityValues[k] = max(localDigitSimilarity)
                digitSimilarityKeys[k] = localDigitSimilarity.index(max(localDigitSimilarity))
            #print(digitSimilarityValues, " " ,digitSimilarityKeys)
                #imageSubRegion.show()
            if digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))] < (len(alphabet) - variantsOfSymbol):
                digitsFromImage += str(digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))] // variantsOfSymbol)
    return digitsFromImage


def sampleImage(image, sampleRegion, sizeOfSample, sampleRate):
    for i in range(math.floor((sampleRegion[2] - sampleRegion[0] - sizeOfSample[0] + 1) / sampleRate[0])):
        for j in range(math.floor((sampleRegion[3] - sampleRegion[1] - sizeOfSample[1] + 1) / sampleRate[1])):
            sampledRegion = image.crop((sampleRegion[0] + i * sampleRate[0],
                                        sampleRegion[1] + j * sampleRate[1],
                                        sampleRegion[2] + i * sampleRate[0] + sizeOfSample[0],
                                        sampleRegion[3] + j * sampleRate[1] + sizeOfSample[1]))
            return sampledRegion


def writeListToFile(data, filePath):
    file = open(filePath, "a")
    file.write(",".join(str(s) for s in data))
    data.clear()
    file.close()


def writeDataToFile(sourcePath, destinationPath, amountAlphabet, priceAlphabet, width1, width2, digitsFromImage):
    for i in range(27):
        digitsFromImage.append(getDigitsFromImage(sourcePath + "\Amount" + str(i) + ".bmp", amountAlphabet, 2, width1))
    writeListToFile(digitsFromImage, destinationPath)
    file = open(destinationPath, "a")
    file.write("," + sourcePath[sourcePath.index("\\T") + 1:])
    file.write("\n")
    file.close()
    for i in range(27):
        digitsFromImage.append(getDigitsFromImage(sourcePath + "\Price" + str(i) + ".bmp", priceAlphabet, 2, width2))
    writeListToFile(digitsFromImage, destinationPath)
    file = open(destinationPath, "a")
    file.write("\n")
    file.close()