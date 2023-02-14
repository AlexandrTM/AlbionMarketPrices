from ImageToDigits import *


basicPath = r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices"
resourcePath = basicPath + "\data\Resource"
digitsPath = basicPath + "\data\Digits"

amountAlphabetFileList = glob(digitsPath + "\Amount\*.bmp")
priceAlphabetFileList = glob(digitsPath + "\Price\*.bmp")
if len(amountAlphabetFileList) > 0:
    amountAlphabetDigits = ["digit" + str(i) for i in range(len(amountAlphabetFileList))]
    for i in range(len(amountAlphabetFileList)):
        amountAlphabetDigits[i] = Image.open(digitsPath + "\Amount\Digit" + str(i) + ".bmp")
if len(priceAlphabetFileList) > 0:
    priceAlphabetDigits = ["digit" + str(i) for i in range(len(priceAlphabetFileList))]
    for i in range(len(priceAlphabetFileList)):
        priceAlphabetDigits[i] = Image.open(digitsPath + "\Price\Digit" + str(i) + ".bmp")


def main():
    resourceNames = ["WOOD", "ROCK", "ORE", "FIBER", "HIDE"]
    resourcePaths = []
    for i in range(5, 9):
        for j in range(len(resourceNames)):
            resourcePaths.append(resourcePath + "\T" + str(i) + "_" + resourceNames[j])

    # for i in range(9):
    #     writeDataToFile(resourcePaths[i], filePath, amountAlphabetDigits, priceAlphabetDigits, 6, 6, digitsFromImage)
    # for i in range(9, len(resourcePaths)):
    #     writeDataToFile(resourcePaths[i], filePath, amountAlphabetDigits, priceAlphabetDigits, 6, 7, digitsFromImage)
    # digitsFromImage.append(getDigitsFromImage(resourcePath + "\T5_WOOD\Price" + str(16) + ".bmp", amountAlphabetDigits, 2, 6, 1))

    # for i in range(len(resourcePaths)):
    #     for j in range(27):
    #         splitImageIntoDigits(resourcePaths[i] + "\Price" + str(j) + ".bmp")
    #         splitImageIntoDigits(resourcePaths[i] + "\Amount" + str(j) + ".bmp")

    digitsFromImage = []
    changedImagesPath = r"C:\Users\sasha\Desktop\changedImages"
    changedAmountImagesPaths = glob(changedImagesPath + "\*\*\Amount*.bmp")
    changedPriceImagesPaths = glob(changedImagesPath + "\*\*\Price*.bmp")
    for i in range(len(changedAmountImagesPaths)):
        digitsFromImage.append(detectDigitsInImage(changedAmountImagesPaths[i], amountAlphabetDigits))
        digitsFromImage.append(detectDigitsInImage(changedPriceImagesPaths[i], priceAlphabetDigits))

    filePath = r"C:\Users\sasha\Desktop\resourceData.csv"
    file = open(filePath, "w")
    file.close()


if __name__ == '__main__':
    main()
