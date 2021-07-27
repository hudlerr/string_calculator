import string_calculator

def test_1():
    tmp = string_calculator.StringCalculator()
    inputVal = "+,3,5"
    expRes = ["OPERATOR", "NUMBER", "NUMBER"]

    res = tmp.parse(inputVal)

    assert res == expRes

def test_2():
    tmp = string_calculator.StringCalculator()
    inputVal = "x,x,x"
    expRes = ["INVALID_OPERATOR", "INVALID_NUMBER", "INVALID_NUMBER"]

    res = tmp.parse(inputVal)

    assert res == expRes

def test_3():
    tmp = string_calculator.StringCalculator()
    inputVal = "+,x,x"
    expRes = ["OPERATOR", "INVALID_NUMBER", "INVALID_NUMBER"]

    res = tmp.parse(inputVal)

    assert res == expRes        
    