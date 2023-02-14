from ImageToDigits import *


basicPath = r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices"
resourcePath = basicPath + "\data\Resource"
digitsPath = basicPath + "\data\Digits"

amountAlphabetPathsPerNum = []
priceAlphabetPathsPerNum = []

amountAlphabetDigits = [[] for i in range(10)]
priceAlphabetDigits = [[] for i in range(10)]


for i in range(10):
    amountAlphabetPathsPerNum.append(len(glob(digitsPath + "\Amount\\" + str(i) + "\*.bmp")))
    priceAlphabetPathsPerNum.append(len(glob(digitsPath + "\Price\\" + str(i) + "\*.bmp")))
for i in range(10):
    for j in range(amountAlphabetPathsPerNum[i]):
        amountAlphabetDigits[i].append(Image.open(digitsPath + "\Amount\\" + str(i) + "\Digit" + str(j) + ".bmp"))
    for j in range(priceAlphabetPathsPerNum[i]):
        priceAlphabetDigits[i].append(Image.open(digitsPath + "\Price\\" + str(i) + "\Digit" + str(j) + ".bmp"))
# print(len(priceAlphabetDigits[1]))

# amountAlphabetFileList = glob(digitsPath + "\Amount\*.bmp")
# priceAlphabetFileList = glob(digitsPath + "\Price\*.bmp")
# if len(amountAlphabetFileList) > 0:
#     amountAlphabetDigits = ["digit" + str(i) for i in range(len(amountAlphabetFileList))]
#     for i in range(len(amountAlphabetFileList)):
#         amountAlphabetDigits[i] = Image.open(digitsPath + "\Amount\Digit" + str(i) + ".bmp")
# if len(priceAlphabetFileList) > 0:
#     priceAlphabetDigits = ["digit" + str(i) for i in range(len(priceAlphabetFileList))]
#     for i in range(len(priceAlphabetFileList)):
#         priceAlphabetDigits[i] = Image.open(digitsPath + "\Price\Digit" + str(i) + ".bmp")


def main():
    filePath = r"C:\Users\sasha\Desktop\resourceData.csv"
    file = open(filePath, "w")
    file.close()

    digitsFromImage = []
    changedImagesPath = r"C:\Users\sasha\Desktop\changedImages\Resource"
    changedImagesPaths = []
    changedAmountImagesPaths = glob(changedImagesPath + "\*\Amount*.bmp")
    changedPriceImagesPaths = glob(changedImagesPath + "\*\Price*.bmp")

    resourceNames = ["WOOD", "ROCK", "ORE", "HIDE", "FIBER"]
    resourcePaths = []
    for i in range(5, 9):
        for j in range(len(resourceNames)):
            resourcePaths.append(resourcePath + "\T" + str(i) + "_" + resourceNames[j])
    for i in range(5, 9):
        for j in range(len(resourceNames)):
            changedImagesPaths.append(changedImagesPath + "\T" + str(i) + "_" + resourceNames[j])


    # for i in range(len(resourcePaths)):
    #     for j in range(27):
    #         splitImageIntoDigits(resourcePaths[i] + "\Price" + str(j) + ".bmp")
    #         splitImageIntoDigits(resourcePaths[i] + "\Amount" + str(j) + ".bmp")

    for i in range(len(changedImagesPaths)):
        for j in range(27):
            digitsFromImage.append(detectDigitsInImage(changedImagesPaths[i] + "\Amount" + str(j) + ".bmp", amountAlphabetDigits))
        writeListDataToFile(filePath, digitsFromImage)
        digitsFromImage.clear()
        for j in range(27):
            digitsFromImage.append(detectDigitsInImage(changedImagesPaths[i] + "\Price" + str(j) + ".bmp", priceAlphabetDigits))
        writeListDataToFile(filePath, digitsFromImage)
        digitsFromImage.clear()
    # digitsFromImage.append(detectDigitsInImage(r"C:\Users\sasha\Desktop\changedImages\Resource\T5_WOOD" + "\Price" + str(25) + ".bmp", priceAlphabetDigits))
    # writeListDataToFile(filePath, digitsFromImage)
    # digitsFromImage.clear()



if __name__ == '__main__':
    main()
