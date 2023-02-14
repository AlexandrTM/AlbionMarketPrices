import numpy as np
import math
from glob import glob
from PIL import Image, ImageChops


def getImageDifference(image1, image2):
    difference = ImageChops.difference(image1, image2)
    return 100 - np.mean(np.array(difference))


def getDigitsFromImage(imagePath, alphabet, variantsOfSymbol, sampleWidth, scanOrder):
    image = Image.open(imagePath)
    width, height = image.size
    digitSimilarityValues = [0] * 4
    digitSimilarityKeys = [0] * 4
    localDigitSimilarity = [float(0)] * len(alphabet)
    digitsFromImage = str()

    sampledImageRegions = []
    sampleImage(image, [-1, 2, width, 9], [sampleWidth, 7], [1, 1], scanOrder, sampledImageRegions)
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


def sampleImage(image, sampleRegion, sizeOfSample, sampleRate, scanOrder, sampledRegions):
    for i in range(math.floor((sampleRegion[2] - sampleRegion[0] - sizeOfSample[0] + 1) / sampleRate[0]))[::scanOrder]:
        for j in range(math.floor((sampleRegion[3] - sampleRegion[1] - sizeOfSample[1] + 1) / sampleRate[1]))[::scanOrder]:
            sampledRegions.append(image.crop((sampleRegion[0] + i * sampleRate[0] - min(i, sampleRegion[0] * -1),
                                              sampleRegion[1] + j * sampleRate[1] - min(j, sampleRegion[1] * -1),
                                              sampleRegion[2] + i * sampleRate[0] + sizeOfSample[0],
                                              sampleRegion[3] + j * sampleRate[1] + sizeOfSample[1])))
    return sampledRegions


def writeListToFile(data, filePath):
    file = open(filePath, "a")
    file.write(",".join(str(s) for s in data))
    data.clear()
    file.close()


def writeDataToFile(sourcePath, destinationPath, amountAlphabet, priceAlphabet,
                    sampleWidth1, sampleWidth2, digitsFromImage):
    for i in range(5):
        digitsFromImage.append(getDigitsFromImage(sourcePath + "\Amount" + str(i) + ".bmp", amountAlphabet, 2, sampleWidth1, 1))
    writeListToFile(digitsFromImage, destinationPath)
    file = open(destinationPath, "a")
    file.write("," + sourcePath[sourcePath.index("\\T") + 1:])
    file.write("\n")
    file.close()
    for i in range(5):
        digitsFromImage.append(getDigitsFromImage(sourcePath + "\Price" + str(i) + ".bmp", priceAlphabet, 2, sampleWidth2, -1))
    writeListToFile(digitsFromImage, destinationPath)
    file = open(destinationPath, "a")
    file.write("\n")
    file.close()