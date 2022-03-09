import pytest
import itertools
from kombinacja_sejfu.sejf import prework_input, check_input, \
                                    check_ascending_numbers, check_same_adjesent, \
                                    get_number_of_passwords, get_generated_numbers

"""
Dla zakresu wejściowego: 110012-365579
111111 spełnia te kryteria (podwójna 11, nigdy nie maleje).
223450 nie spełnia tych kryteriów (malejąca para cyfr 50).
123789 nie spełnia tych kryteriów (brak podwójnych).
55667788 nie spełnia tych kryteriów (liczba jest większa od maksymalnej wartości zakresu wejściowego: 365579

"""

def test_prework_input_returns_list():
    assert prework_input('265275') == ['265275']
    assert prework_input('110012-365579') == ['110012', '365579']


def test_check_input_fails_with_invalid_input():
    assert check_input(['110012', '365579', '265275']) == False
    assert check_input(['110012']) == False
    assert check_input(['110A012', '365579']) == False
    assert check_input(['110012', '3+65579']) == False
    assert check_input(['110012', '36579']) == False
    assert check_input(['11012', '36679']) == False
    assert check_input(['365579', '265275']) == False

def test_check_input_with_valid_input():
    assert check_input(['110012', '265275']) == True

def test_check_ascending_numbers_returns_false_with_invalid_input():
    assert check_ascending_numbers('123456648') == False
    assert check_ascending_numbers('12345648') == False

def test_check_ascending_numbers_returns_true_with_valid_input():
    assert check_ascending_numbers('12345678') == True
    assert check_ascending_numbers('1222345678') == True
    assert check_ascending_numbers('1245678') == True

def test_check_same_adjesent_returns_false_with_no_adjesent():
    assert check_same_adjesent('12345678') == False

def test_check_same_adjesent_returns_true_with_adjesent():
    assert check_same_adjesent('122345678') == True

def test_get_generated_numbers():
    assert list(itertools.islice(get_generated_numbers('265275-781584'), 3)) == [266666, 266667, 266668]
    assert list(itertools.islice(get_generated_numbers('123455-123500'), 3)) == [123455, 123466, 123477]

def test_get_number_of_passwords_default_values():
    assert get_number_of_passwords() == 960

def test_get_number_of_passwords():
    assert get_number_of_passwords('123456-123499') == 4