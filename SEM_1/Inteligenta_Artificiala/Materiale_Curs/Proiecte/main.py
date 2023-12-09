def main():
    numlist = list()
    while(True):
        inp = input("Introduceti un numar: ")
        if inp == 'gata':break
        value = float(inp)
        numlist.append(value)
    media = sum(numlist) / len(numlist)
    print('Media: ', media)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
