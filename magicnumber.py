
def testingsomething():
    userguess=int(input("Enter a number 1-10 until you guess the magic number."))
    magicnumber=4
    message=str(magicnumber)+" is the magic number!"
    if userguess == magicnumber:
            print(message)
    else:
        print("Nope. Try again.")
        testingsomething()

testingsomething()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
