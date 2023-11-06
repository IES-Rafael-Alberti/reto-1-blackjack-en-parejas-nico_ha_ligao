import pytest
from src.blackjat import pedir_carta

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    (0, "A"),
    (1, "2"),
    (2, "3"),
    (3, "4"),
    (4, "5"),
    (5, "6"),
    (6, "7"),
    (7, "8"),
    (8, "9"),
    (9, "0"),
    (10, "J"),
    (11, "K"),
    (12, "Q")
    ]
)
def test_pedir_carta_params(input_n1, expected):
    assert pedir_carta(input_n1) == expected