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
            if getImageDifference(image.crop((i, 0, i + 1, image.size[1])), splitters[j]) > 85:
                for k in range(image.size[1]):
                    imagePixels[i, k] = (255, 0, 0)
    image = image.crop((0, 2, image.size[0], 9))
    image.save(r"C:\Users\sasha\Desktop\changedImages" + imagePath[imagePath.index("\\Resource"):])


def detectDigitsInImage(imagePath, alphabet):
    image = Image.open(imagePath)
    #imageRegion = Image.new("RGB", (0, 0))
    imageWidth, imageHeight = image.size
    #imagePixels = image.load()
    digitsInImage = str()
    i = 0
    while i < imageWidth:
        imagePixels = image.load()
        if imagePixels[i, 0] == (255, 0, 0):
            #imageRegion = imageRegion.resize((max(i, 1), image.size[1]))
            imageRegion = image.crop((0, 0, max(i, 1), image.size[1]))

            #imageRegion.paste(image.crop((0, 0, i, image.size[1])))
            #imageRegion.show()
            #print(imageRegion.size)
            if calculateAverageColorOfImage(imageRegion) != [255, 0, 0]:
                digitsInImage += findDigitInImage(imageRegion, alphabet)
            if imageRegion.size[0] == 10:
                digitsInImage += findDigitInImage(imageRegion.crop((5, 0, imageRegion.size[0], imageRegion.size[1])), alphabet)
            image = image.crop((i + 1, 0, image.size[0], image.size[1]))
            imageWidth -= imageRegion.size[0] + 1
            i = 0
            continue
        i += 1
    return digitsInImage


def findDigitInImage(image, alphabet):
    digitSimilarityValues = [[] for i in range(len(alphabet))]
    digitSimilarityValuesPerVariant = []
    for i in range(len(alphabet)):  # digit
        for j in range(len(alphabet[i])):  # variant of digit
            digitSimilarityValues[i].append(getImageDifference(image, alphabet[i][j]))
    for i in range(len(alphabet)):
        digitSimilarityValuesPerVariant.append(max(digitSimilarityValues[i]))

    digit = str(digitSimilarityValuesPerVariant.index(max(digitSimilarityValuesPerVariant)))
    return digit


def calculateAverageColorOfImage(image):
    imagePixels = image.load()
    sumRed, sumGreen, sumBlue = 0, 0, 0
    pixelCount = image.size[0] * image.size[1]

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = imagePixels[i, j]
            sumRed += pixel[0]
            sumGreen += pixel[1]
            sumBlue += pixel[2]
    avgRed = int(sumRed / pixelCount)
    avgGreen = int(sumGreen / pixelCount)
    avgBlue = int(sumBlue / pixelCount)
    avgPixelColor = [avgRed, avgGreen, avgBlue]
    return avgPixelColor


def sampleImage(image, sampleRegion, sampleExtent, sampleOffset, sampleRate, scanOrder, sampledRegions):
    for i in range(math.floor((sampleRegion[2] - sampleRegion[0] - sampleExtent[0] + 1) / sampleRate[0]))[::scanOrder]:
        for j in range(math.floor((sampleRegion[3] - sampleRegion[1] - sampleExtent[1] + 1) / sampleRate[1])):
            sampledRegions.append(image.crop((sampleRegion[0] + i * sampleRate[0] - min(i, sampleOffset[0] * -1),
                                              sampleRegion[1] + j * sampleRate[1] - min(j, sampleOffset[1] * -1),
                                              sampleRegion[0] + i * sampleRate[0] + sampleExtent[0],#*****
                                              sampleRegion[1] + j * sampleRate[1] + sampleExtent[1])))#*****
    return sampledRegions


def writeListDataToFile(filePath, listData):
    file = open(filePath, "a")
    for i in range(len(listData)):
        file.write(str(listData[i]) + ",")
    file.write("\n")
    file.close()
