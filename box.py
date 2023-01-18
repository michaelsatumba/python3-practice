
def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string length 1.')
    print(symbol * width)

    # assert len(symbol) == 1, 'Length should be 1'

    for i in range(height - 2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)

    

boxPrint('$', 15, 5)
