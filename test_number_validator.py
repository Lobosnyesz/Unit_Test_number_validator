"""
TESZTELENDŐ FELADAT - NumberValidator osztály unit tesztek

A feladat: Írj unit teszteket a NumberValidator osztály metódusaihoz!
Használd a különböző assert típusokat!
"""

import pytest
from number_validator import NumberValidator


# ============================================================================
# FELADAT: Írd meg az alábbi teszteket!
# ============================================================================

def test_is_even_equal():
    """1.1 Assert equal - páros szám ellenőrzés"""
    validator = NumberValidator()
    # TODO: Hívd meg az is_even metódust páros számmal
    result = validator.is_even(20)
    # TODO: Ellenőrizd, hogy az eredmény True
    assert result == True
    


def test_is_even_not_equal():
    """1.2 Assert not equal - páratlan szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_even metódust páratlan számmal
    result = validator.is_even(21)
    # TODO: Ellenőrizd, hogy az eredmény NEM egyenlő True-val
    assert result != True


def test_is_even_with_zero():
    """1.3 Speciális eset - nulla kezelése"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_even metódust 0-val
    result = validator.is_even(0)
    # TODO: Ellenőrizd, hogy az eredmény True-e?
    assert result == True


def test_is_positive_greater_than():
    """2.1 Assert > - pozitív szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_positive metódust pozitív számmal
    result=validator.is_positive(10)
    # TODO: Ellenőrizd, hogy az eredmény True-e?
    assert result == True


def test_is_positive_with_negative():
    """2.2 Negatív szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_positive metódust pozitív számmal
    resultp = validator.is_positive(13)
    # TODO: Hívd meg az is_positive metódust negatív számmal
    resultn= validator.is_positive(-12)
    # TODO: Ellenőrizd, hogy az eredmény True vagy False?
    assert resultn == False
    assert resultp == True
    pass


def test_is_in_range_less_than():
    """3.1 Assert <, <= - tartományon belüli ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_in_range metódust egy számmal, ami a tartományban van
    result = validator.is_in_range(2,1,5)
    # TODO: Ellenőrizd, hogy az eredmény True
    assert result == True
    pass


def test_is_in_range_out_of_range():
    """3.2 Assert <, <= - tartományon kívüli ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_in_range metódust egy számmal, ami a tartományon kívül van
    result = validator.is_in_range(10, 1, 5)
    # TODO: Ellenőrizd, hogy az eredmény True
    assert result != True


def test_get_absolute_value_isinstance():
    """4. Assert isinstance - típus ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg a get_absolute_value metódust negatív számmal (pl. -5)
    result = validator.get_absolute_value(-5)
    # TODO: Ellenőrizd, hogy az eredmény integer típusú
    assert isinstance(result,int) is True
    # TODO: Ellenőrizd, hogy az eredmény NEM string típusú
    assert isinstance(result,str) is False


def test_is_divisible_by_true_false():
    """5. Assert True/False - oszthatóság ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_divisible_by metódust olyan számmal, ami osztható egymással
    result = validator.is_divisible_by(10,2)
    # TODO: Ellenőrizd, hogy az eredmény True
    assert result is True
    # TODO: Hívd meg olyan számmal, ami NEM osztható (maradékos osztás)
    result = validator.is_divisible_by(10,3)
    # TODO: Ellenőrizd, hogy az eredmény False
    assert result is False


def test_square_none():
    """6. Assert None - None ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg a square metódust None értékkel
    result = validator.square(None)
    # TODO: Ellenőrizd, hogy az eredmény NEM None
    assert result != None
    # TODO: Ellenőrizd, hogy az eredmény 0-e?
    assert result == 0


def test_is_prime_multiple_asserts():
    """7. Több assert egy tesztben - prímszám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    validator = NumberValidator()
    # TODO: Hívd meg az is_prime metódust prímszámmal
    result = validator.is_prime(11)
    # TODO: Ellenőrizd több assert-tel:
    #      - Az eredmény True
    assert result == True
    #      - Az eredmény boolean típusú
    assert isinstance(result,bool) is True
    #      - Az eredmény nem egyenlő False-szal
    assert result != False
    pass

