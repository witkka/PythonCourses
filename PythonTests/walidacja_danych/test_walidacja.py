import re
import pytest

from walidacja_danych.walidacja import uniform_scans, get_parameter_number, \
                                        get_cid, validate_parameter, \
                                        get_valid_scans, get_valid_scans_number



scan1 = """iyr:2016 hgt:187cm byr:1980 pid:977322718
eyr:2027 ecl:brn hcl:#ceb3a1"""

scan2 = """hcl:#d125e3 iyr:2016 byr:1982 eyr:2027
hgt:154cm
pid:365548961"""

scan3 = """eyr:2023 byr:1974 pid:067761346 cid:178 ecl:hzl iyr:2020 hgt:168cm hcl:#6b5442"""

example = scan1+'\n\n'+scan2+'\n\n\n\n'+scan3
example2 = scan1+'\n\n'+scan2

def test_uniform_scans_has_no_blank_lines():
    assert len(re.findall(r'(\n){2,}', ' '.join(uniform_scans(example)))) == 0

def test_get_parameter_number():
    assert get_parameter_number(scan1) == 7
    assert get_parameter_number(scan2) == 6
    assert get_parameter_number(scan3) == 8

def test_get_cid():
    assert get_cid(scan1) == False
    assert get_cid(scan2) == False
    assert get_cid(scan3) == True

def test_validate_parameter():
    assert validate_parameter(scan1) == False
    assert validate_parameter(scan2) == False
    assert validate_parameter(scan3) == True

def test_get_valid_scans():
    assert list(get_valid_scans(example)) == ['eyr:2023 byr:1974 pid:067761346 cid:178 ecl:hzl iyr:2020 hgt:168cm hcl:#6b5442']
    assert list(get_valid_scans(example2)) == []

def test_valid_scan_number():
    assert get_valid_scans_number(example) == 1
    assert get_valid_scans_number(example2) == 0