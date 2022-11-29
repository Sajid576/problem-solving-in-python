
def test(actual, expected):
    if(type(actual) == list and type(expected) == list):
        ck = 0
        for i in range(len(actual)):
            if(actual[i] != expected[i]):
                ck = 1
                break
        if(ck == 1):
            failMessage = " Should be: "+str(expected)
            print("❌" + failMessage, "\nGetting:", actual)
        else:
            print("✅ Passed")
    else:
        try:
            assert actual == expected
            print("✅ Passed")
        except:
            failMessage = " Should be: "+str(expected)
            print("❌" + failMessage, "\nGetting:", actual)
