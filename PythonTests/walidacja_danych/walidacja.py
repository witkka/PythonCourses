"""
Skanery dokumentów obsługują 8 parametrów.
Dokument zostanie uznany za ważny, jeśli wszystkie parametry zostały uzupełnione
lub jeżeli jedynym brakującym parametrem jest cid.
Dane dokumentów są przekazywane w plikach txt.
Każdy dokument jest reprezentowany jako sekwencja par klucz:wartość
oddzielonych spacjami lub znakami nowej linii.
Dokumenty są oddzielone pustymi liniami.

Rozwiązane sprawdza dane o dokumentach podane w pliku txt,
zwraca wynik informujący o liczbie ważnych dokumentów.
"""

import re
import pathlib

# otwiera plik .txt zawierający dokumenty
def load_input_file():
    with open(pathlib.Path(__file__).parent / 'plik_wejsciowy.txt') as input_file:
        return input_file.read()

# usuwa puste linie, zwraca znormalizowaną listę
def uniform_scans(scan_input: str) -> list:
    blank_line_regex = r"(?:\r?\n){2,}"
    return re.split(blank_line_regex, scan_input.strip())

# zwraca liczbę parametrów w jednym dokumencie
def get_parameter_number(parameter: str) -> int:
    return len(parameter.split())

# zwraca True, jeśli jeden z parametrów to cid
def get_cid(parameter: str) -> bool:
    for elem in parameter.split():
        cid_regex = r"^(cid:)"
        if re.match(cid_regex, elem):
            return True
    return False

# zwraca True jeśli dokument spełnia wymagania
def validate_parameter(parameter: list) -> bool:
    if get_parameter_number(parameter) == 8: # wszystkie parametry uzupełnione
        return True
    if get_parameter_number(parameter) == 7: # brakuje tylko jednego parametru
        return get_cid(parameter) # jest obecny parametr cid
    return False

# tworzy generator z ważnymi dokumentami
def get_valid_scans(text):
    for single_scan in uniform_scans(text):
        if validate_parameter(single_scan) == True:
            yield single_scan

# zwraca wynik informujący o liczbie ważnych dokumentów
def get_valid_scans_number(text) -> int:
    return len(list(get_valid_scans(text)))

# zwraca wynik informujący o liczbie ważnych dokumentów w dokumencie tekstowym
# dołączonym do zadania
get_valid_scans_number(load_input_file())