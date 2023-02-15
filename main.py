from ImageToDigits import *


def main():
    basicPath = r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices"
    citiesBasicPath = basicPath + "\data\Royal Cities"
    digitsPath = basicPath + "\data\Digits"
    processedImagesBasicPath = basicPath + "\data\Processed images\Royal Cities"
    filePath = r"C:\Users\sasha\Desktop\resourceData.csv"

    rawResourceNames = ["WOOD", "ROCK", "ORE", "HIDE", "FIBER"]
    outputResourceNames = ["PLANKS", "STONEBLOCK", "METALBAR", "LEATHER", "CLOTH"]
    materialNames = ["RUNE", "SOUL", "RELIC", "SHARD_AVALONIAN"]
    cityNames = ["Lymhurst", "Bridgewatch", "Martlock", "Thetford", "Fort Sterling"]
    itemCategories = ["Resource", "Materials"]
    itemPaths = []
    processedImagesPaths = []

    amountAlphabetPathsPerNum = []
    priceAlphabetPathsPerNum = []

    amountAlphabetDigits = [[] for i in range(10)]
    priceAlphabetDigits = [[] for i in range(10)]

    # digits loading
    for i in range(10):
        amountAlphabetPathsPerNum.append(len(glob(digitsPath + "\Amount\\" + str(i) + "\*.bmp")))
        priceAlphabetPathsPerNum.append(len(glob(digitsPath + "\Price\\" + str(i) + "\*.bmp")))
        for j in range(amountAlphabetPathsPerNum[i]):
            amountAlphabetDigits[i].append(Image.open(digitsPath + "\Amount\\" + str(i) + "\Digit" + str(j) + ".bmp"))
        for j in range(priceAlphabetPathsPerNum[i]):
            priceAlphabetDigits[i].append(Image.open(digitsPath + "\Price\\" + str(i) + "\Digit" + str(j) + ".bmp"))

    # for i in range(len(materialNames)):
    #     createItemPaths(materialNames[i], 5, 8, cityNames[3], itemCategories[1],
    #                     citiesBasicPath, processedImagesBasicPath, itemPaths, processedImagesPaths)

    for i in range(len(rawResourceNames)):
        createItemPaths(rawResourceNames[i], 5, 8, cityNames[3], itemCategories[0] + "\Raw",
                        citiesBasicPath, processedImagesBasicPath, itemPaths, processedImagesPaths)

    # splitting images into digits
    # for i in range(len(itemPaths)):
    #     for j in range(27):
    #         splitImageIntoDigits(itemPaths[i] + "\Price" + str(j) + ".bmp",
    #                              processedImagesPaths[i] + "\Price" + str(j) + ".bmp")
    #         splitImageIntoDigits(itemPaths[i] + "\Amount" + str(j) + ".bmp",
    #                              processedImagesPaths[i] + "\Amount" + str(j) + ".bmp")

    # digits detection
    file = open(filePath, "w")
    file.close()
    digitsFromImage = []
    for i in range(len(processedImagesPaths)):
        for j in range(27):
            digitsFromImage.append(detectDigitsInImage(
                processedImagesPaths[i] + "\Amount" + str(j) + ".bmp", amountAlphabetDigits))
        writeListDataToFile(filePath, digitsFromImage)
        digitsFromImage.clear()
        file = open(filePath, "a")
        file.write(str(processedImagesPaths[i][processedImagesPaths[i].index("Raw\\") + 4:]) + "\n")
        file.close()
        for j in range(27):
            digitsFromImage.append(detectDigitsInImage(
                processedImagesPaths[i] + "\Price" + str(j) + ".bmp", priceAlphabetDigits))
        writeListDataToFile(filePath, digitsFromImage)
        digitsFromImage.clear()
        file = open(filePath, "a")
        file.write("\n")
        file.close()

    # digitsFromImage.append(detectDigitsInImage(r"C:\Users\sasha\Desktop\changedImages\Resource\T5_WOOD" + "\Price" + str(25) + ".bmp", priceAlphabetDigits))
    # writeListDataToFile(filePath, digitsFromImage)
    # digitsFromImage.clear()


if __name__ == '__main__':
    main()
