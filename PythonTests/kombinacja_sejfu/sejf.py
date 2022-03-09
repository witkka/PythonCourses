"""
Kod do sejfu to liczba sześciocyfrowa.
Kombinacje, które są poprawne obejmują warunki:
1) Przynajmniej dwie sąsiednie cyfry są takie same (np. 22 w 122345).
2) Idąc od lewej do prawej, cyfry nigdy się nie zmniejszają;
one tylko rosną lub pozostają takie same (jak 111123 lub 135679).
Należy pozwolić zdefiniować zakres, w którym powinny zmieścić się poprawne kody.
Rozwiązanie sprawdza dla zakresu: 265275-781584,
liczbę kodów spełniających powyższe warunki.
"""

# przyjmuje zakres w formie str, zwraca wieloelementową listę
def prework_input(n_range: str) -> list:
    return n_range.split('-')

# zwraca True jeśli dane wejściowe są poprawne
def check_input(range_list: list) -> bool:
    if len(range_list) !=2: # False jeśli jest więcej elementów niż 2
        return False
    else:
        numberA = range_list[0]
        numberB = range_list[1]
        if not numberA.isalnum() or not numberB.isalnum(): # False jeśli wartości nie są liczbami
            return False
        if len(numberA)!=6 or len(numberB) != 6: # False jeśli liczba cyfr w wartościach zakresu jest nieprawidłowa
            return False
        if int(numberA) > int(numberB): # False jeśli wartość końcowa zakresu jest większa od początkowej
            return False
    return True

# sprawdza, czy wszystkie cyfry są w kolejności niemalejącej
def check_ascending_numbers(number: str) -> bool:
    if number == ''.join(sorted(number)):
        return True
    return False

# zwraca true, jeśli są obok siebie dwie takie same cyfry
def check_same_adjesent(number):
    if len(number) >1:
        if number[0]==number[1]:
            return True
        else:
            return check_same_adjesent(number[1:])
    return False

# zwraca generator liczb z zakresu,
# liczby spełniają warunki zadania
def get_generated_numbers(n_range):
    normalized_input = prework_input(n_range)
    if check_input(normalized_input) == True: # właściwy zakres
        numberA, numberB = int(normalized_input[0]), int(normalized_input[1])
        for number in range(numberA, numberB+1): # zakres z włączeniem obu wartości granicnych
            if check_ascending_numbers(str(number)): # cyfry niemalejące
                if check_same_adjesent(str(number)): # min 1 para sąsiednich cyfr taka sama
                    yield number

# rozwiązanie zadania, funkcja zwraca liczbę kodów spełniających powyższe warunki
def get_number_of_passwords(n_range='265275-781584') -> int:
    return len(list(get_generated_numbers(n_range)))
