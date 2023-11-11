import pytest
from src.blackjat import suma_cartas

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    ("A", 10),
    ("87", 15),
    ("02", 12),
    ("23", 5),
    ("776", 20),
    ("2234", 11),
    ("KJ", 20),
    ("Q7", 17),
    ("0A", 20),
    ("50A", 16),
    ("88", 16),
    ("A83", 21),
    ("AQQ", 21),
    ("AAA", 21),
    ("AK8", 19),
    ("Q23", 15),
    ("JJ2", 22)
    ]
)
def test_suma_cartas_params(input_n1, expected):
    assert suma_cartas(input_n1) == expected