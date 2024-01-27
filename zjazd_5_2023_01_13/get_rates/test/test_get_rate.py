from rates.get_rate import get_rate
import pytest


def test_get_rates():
    result = get_rate("EUR")    #jeśli robimy dependancy injection to w nawiasie wpisujemy ("EUR", udawany_internet) Zamiast daych ze strony NBP weźmie dane z tego co my stworzyliśmy
    assert result > 0


