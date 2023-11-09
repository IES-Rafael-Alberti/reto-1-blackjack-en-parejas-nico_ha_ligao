import pytest
from src.blackjat import ronda1

@pytest.mark.parametrize(
    "input_n1,expected",
    [
    (9, 10),
    (14, 15),
    (11, 12),
    (4, 5),
    (19, 20),
    (10, 11),
    (0, 1),
    (334, 335),
    (34, 35),
    (15, 16),
    (67, 68),
    (20, 21),
    (18, 19),
    (28, 29),
    (21, 22)
    ]
)
def test_ronda1_cartas_params(input_n1, expected):
    assert ronda1(input_n1) == expected