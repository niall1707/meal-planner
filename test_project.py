from project import check_age, Bmi, Bmi_range # type: ignore

def test_check_age():
    assert check_age("20") == True
    assert check_age("10") == True

def test_Bmi():
    assert Bmi(170,50) == 17.301038062283737
    assert Bmi(100, 100) == 100.0

def test_Bmi_range():
    assert Bmi_range(20) == "Healthy"
    assert Bmi_range(40) == "Obese"