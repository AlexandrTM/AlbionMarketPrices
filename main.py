from ImageToDigits import *


def main():
    basicPath = r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices"
    citiesBasicPath = basicPath + "\data\Royal Cities"
    digitsPath = basicPath + "\data\Digits"
    processedImagesBasicPath = basicPath + "\data\Processed images\Royal Cities"
    filePath = r"C:\Users\sasha\Desktop\resourceData.csv"

    splittersPath = r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Digits\Splitters"
    splittersPaths = glob(splittersPath + "\*.bmp")
    splitters = ["" + str(i) for i in range(len(splittersPaths))]
    for i in range(len(splittersPaths)):
        splitters[i] = Image.open(splittersPaths[i])

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

    for i in range(len(cityNames)):
        # for j in range(len(materialNames)):
        #     createItemPaths(materialNames[j], 4, 8, cityNames[i], itemCategories[1],
        #                     citiesBasicPath, processedImagesBasicPath, itemPaths, processedImagesPaths)
        #
        # for j in range(len(rawResourceNames)):
        #     createItemPaths(rawResourceNames[j], 5, 8, cityNames[3], itemCategories[0] + "\Raw",
        #                     citiesBasicPath, processedImagesBasicPath, itemPaths, processedImagesPaths)

        for j in range(len(outputResourceNames)):
            createItemPaths(outputResourceNames[j], 5, 8, cityNames[i], itemCategories[0] + "\Output",
                            citiesBasicPath, processedImagesBasicPath, itemPaths, processedImagesPaths)

    # splitting images into digits
    # for i in range(len(itemPaths)):
    #     for j in range(27):
    #         splitImageIntoDigits(itemPaths[i] + "\Price" + str(j) + ".bmp",
    #                              processedImagesPaths[i] + "\Price" + str(j) + ".bmp", splitters)
    #         splitImageIntoDigits(itemPaths[i] + "\Amount" + str(j) + ".bmp",
    #                              processedImagesPaths[i] + "\Amount" + str(j) + ".bmp", splitters)
    #     print(itemPaths[i][itemPaths[i].index("_") - 2:], " splitted")

    # digits detection
    file = open(filePath, "w")
    file.close()
    digitsFromImage = []
    # for i in range(len(processedImagesPaths)):
    #     for j in range(27):
    #         digitsFromImage.append(detectDigitsInImage(
    #             processedImagesPaths[i] + "\Amount" + str(j) + ".bmp", amountAlphabetDigits))
    #     writeListDataToFile(filePath, digitsFromImage)
    #     digitsFromImage.clear()
    #     file = open(filePath, "a")
    #     file.write(str(processedImagesPaths[i][processedImagesPaths[i].index("_") - 2:]) + "\n")
    #     file.close()
    #     for j in range(27):
    #         digitsFromImage.append(detectDigitsInImage(
    #             processedImagesPaths[i] + "\Price" + str(j) + ".bmp", priceAlphabetDigits))
    #     writeListDataToFile(filePath, digitsFromImage)
    #     digitsFromImage.clear()
    #     file = open(filePath, "a")
    #     file.write("\n")
    #     file.close()
    #     print(processedImagesPaths[i][processedImagesPaths[i].index("_") - 2:], "detected")

    digitsFromImage.append(detectDigitsInImage(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Processed images\Royal Cities\Lymhurst\Resource\Output\T7_LEATHER" + "\Price" + str(15) + ".bmp", priceAlphabetDigits))
    writeListDataToFile(filePath, digitsFromImage)
    # digitsFromImage.clear()
    # splitImageIntoDigits(r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Royal Cities\Fort Sterling\Materials\T5_SOUL\Price24.bmp",
    #                     r"C:\Users\sasha\Desktop\Programms\скрипты\Albion\Market prices\data\Processed images\Royal Cities\Fort Sterling\Materials\T5_SOUL\Price24.bmp", splitters)


if __name__ == '__main__':
    main()
