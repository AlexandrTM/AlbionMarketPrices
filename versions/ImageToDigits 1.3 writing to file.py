import numpy as np
import math
from PIL import Image
from PIL import ImageChops


digit0 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit0.bmp")
digit1 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit1.bmp")
digit2 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit2.bmp")
digit3 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit3.bmp")
digit4 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit4.bmp")
digit5 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit5.bmp")
digit6 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit6.bmp")
digit7 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit7.bmp")
digit8 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit8.bmp")
digit9 = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Digit9.bmp")
digitBlank = Image.open(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\DigitBlank.bmp")

digits = [digit0, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9, digitBlank]


def getImageDifference(image1, image2):
    difference = ImageChops.difference(image1, image2)
    return 100 - np.mean(np.array(difference))


def getDigitsFromImage(imagePath):
    image = Image.open(imagePath)
    width, height = image.size
    digitSimilarityValues = [0] * 4
    digitSimilarityKeys = [0] * 4
    localDigitSimilarity = [float(0)] * len(digits)
    digitsFromImage = str()

    for i in range(math.floor(width / 6) - 1):
    #for i in range(1):
        for j in range(1):# if height needed
            imageRegion = image.crop((i * 6 - min(i, 2), 2, i * 6 + 7, 9))
            for k in range(3):
                imageSubRegion = imageRegion.crop((0 + k, 0, 6 + k, 7))
                for l in range(len(digits)):
                    localDigitSimilarity[l] = getImageDifference(imageSubRegion, digits[l])
                digitSimilarityValues[k] = max(localDigitSimilarity)
                digitSimilarityKeys[k] = localDigitSimilarity.index(max(localDigitSimilarity))
            #print(digitSimilarityValues, " " ,digitSimilarityKeys)
                #imageSubRegion.show()
            if digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))] != 10:
                #print(digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))], end="")
                digitsFromImage += str(digitSimilarityKeys[digitSimilarityValues.index(max(digitSimilarityValues))])
    return digitsFromImage


def writeListToFile(data, filePath):
    file = open(filePath, "a")
    file.write(",".join(str(s) for s in data))
    data.clear()
    file.close()
