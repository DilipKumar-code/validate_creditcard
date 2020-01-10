import validate_creditcard

def test_validateName():
    assert validate_creditcard.validateName("Akash")==True
    assert validate_creditcard.validateName("Maria")==True
    assert validate_creditcard.validateName("9tgfsh")==False
    assert validate_creditcard.validateName("Aka76")==False
    
def test_sum_digits():
    assert validate_creditcard.sum_digits(2)==2
    assert validate_creditcard.sum_digits(9)==9
    assert validate_creditcard.sum_digits(11)==2
    assert validate_creditcard.sum_digits(13)==4

def test_validateCvv():
    assert validate_creditcard.validateCvv("314")==True
    assert validate_creditcard.validateCvv("615")==True
    assert validate_creditcard.validateCvv("91")==False
    assert validate_creditcard.validateCvv("1")==False

def test_validateExpiry():    
    assert validate_creditcard.validateExpiry("09/21")==True
    assert validate_creditcard.validateExpiry("03/25")==True
    assert validate_creditcard.validateExpiry("09/12")==False
    assert validate_creditcard.validateExpiry("09/03")==False

def test_checkCardValidity():
    assert validate_creditcard.checkCardValidity("Akanksha","79927398713","343","03/22")==True
    assert validate_creditcard.checkCardValidity("Adarsh","79927391134","51","04/23")==False
    assert validate_creditcard.checkCardValidity("Kar3tik","79927391134","113","03/27")==False
    assert validate_creditcard.checkCardValidity("Pruthvi","79927391134","823","03/03")==False
    
