import numpy as np
import math
from glob import glob
from PIL import Image, ImageChops


def getImageDifference(image1, image2):
    difference = ImageChops.difference(image1, image2)
    return 100 - np.mean(np.array(difference))


def splitImageIntoDigits(imagePath):
    image = Image.open(imagePath)
    imagePixels = image.load()

    splittersPath = r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Splitters"
    splittersPaths = glob(splittersPath + "\*.bmp")
    splitters = ["splitter" + str(i) for i in range(len(splittersPaths))]
    for i in range(len(splittersPaths)):
        splitters[i] = Image.open(splittersPaths[i])

    for i in range(image.size[0]):
        for j in range(len(splitters)):
            if getImageDifference(image.crop((i, 0, i + 1, image.size[1])), splitters[j]) > 80:
                for k in range(image.size[1]):
                    imagePixels[i, k] = (255, 0, 0)
    image = image.crop((0, 2, image.size[0], 9))
    # image.save(r"C:\Users\sasha\Desktop\changedImages" + imagePath[imagePath.index("\\Resource"):])


def detectDigitsInImage(imagePath, alphabet):
    image = Image.open(imagePath)
    imagePixels = image.load()
    digitsInImage = str()
    for i in range(image.size[0]):
        if imagePixels[i, 0] == (255, 0, 0):
            imageRegion = image.crop((0, 0, i - 1, 7))
            image = image.crop(i + 1, 0, image.size[0], 7)
    return digitsInImage


def getDigitsFromImage(imagePath, alphabet, variantsOfSymbol, sampleWidth, scanOrder):
    image = Image.open(imagePath)
    imageWidth, imageHeight = image.size
    digitSimilarityValues = [0] * 4
    digitSimilarityKeys = [0] * 4
    localDigitSimilarity = [float(0)] * len(alphabet)
    digitsFromImage = str()

    sampledImageRegions = []
    sampleImage(image, [0, 2, imageWidth, 9], [sampleWidth, 7], [-1, 0], [sampleWidth, 1], scanOrder, sampledImageRegions)
    for i in range(len(sampledImageRegions)):
        sampledImageRegions[i].show()
    #     imageSubRegion = sampledImageRegions[i].crop((0 + i, 0, sampleWidth + i, 7))
    #     for j in range(len(alphabet)):
    #         localDigitSimilarity[j] = getImageDifference(imageSubRegion, alphabet[j])
    #     digitSimilarityValues[i] = max(localDigitSimilarity)
    #     digitSimilarityKeys[i] = localDigitSimilarity.index(max(localDigitSimilarity))
    # #print(digitSimilarityValues, " " ,digitSimilarityKeys)
    #     #imageSubRegion.show()
    # if digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))] < (len(alphabet) - variantsOfSymbol):
    #     digitsFromImage += str(digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))] // variantsOfSymbol)
    # print(len(sampledImageRegions))
    # return digitsFromImage


def sampleImage(image, sampleRegion, sampleExtent, sampleOffset, sampleRate, scanOrder, sampledRegions):
    for i in range(math.floor((sampleRegion[2] - sampleRegion[0] - sampleExtent[0] + 1) / sampleRate[0]))[::scanOrder]:
        for j in range(math.floor((sampleRegion[3] - sampleRegion[1] - sampleExtent[1] + 1) / sampleRate[1])):
            sampledRegions.append(image.crop((sampleRegion[0] + i * sampleRate[0] - min(i, sampleOffset[0] * -1),
                                              sampleRegion[1] + j * sampleRate[1] - min(j, sampleOffset[1] * -1),
                                              sampleRegion[0] + i * sampleRate[0] + sampleExtent[0],#*****
                                              sampleRegion[1] + j * sampleRate[1] + sampleExtent[1])))#*****
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