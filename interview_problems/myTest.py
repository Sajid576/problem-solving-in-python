
def myTest(actual,expected):
    try:
        assert actual == expected
        print("✅ Passed")
    except:
        failMessage = " Should be: "+str(expected)
        print("❌" + failMessage)
