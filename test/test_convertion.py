from lib.convertion import Convertion

def test_currency_convertion():
    ammount = 1500
    currency_from = "USD"
    currency_to = "COP"

    currency_value = Convertion().of(currency_from).to(currency_to).convert()
    result = Convertion(ammount).of(currency_from).to(currency_to).convert()
    expected_result = "{0:.2f}".format(ammount*currency_value)
    expected_result = float(expected_result)

    assert result == expected_result

def test_m_to_cm_convertion():
    ammount = 1500
    units_from = "M"
    units_to = "CM"
    units_value = 100

    result = Convertion(ammount).of(units_from).to(units_to).convert()
    expected_result = "{0:.2f}".format(ammount*units_value)
    expected_result = float(expected_result)

    assert result == expected_result

def test_cm3_to_l_convertion():
    ammount = 1500
    units_from = "CM3"
    units_to = "L"
    units_value = 1000

    result = Convertion(ammount).of(units_from).to(units_to).convert()
    expected_result = "{0:.2f}".format(ammount/units_value)
    expected_result = float(expected_result)

    assert result == expected_result
