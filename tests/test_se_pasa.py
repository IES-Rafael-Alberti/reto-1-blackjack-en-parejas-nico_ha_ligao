import pytest
from src.blackjat import se_pasa

@pytest.mark.parametrize(
    "input_n1,input_n2,input_n3,input_n4,input_n5,expected",
    [
    ("A53", "Q39", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - Q39 **se pasa**\nJ2 - Jose - A53 (18)"),
    ("A59", "Q57", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - Q57 **se pasa**\nJ2 - Jose - A59 (15)"),
    ("4567", "Q0", 4, "Pepe", "Jose", "RONDA 4\nJ1 - Pepe - Q0 (20)\nJ2 - Jose - 4567 **se pasa**"),
    ("058", "J49", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - J49 **se pasa**\nJ2 - Jose - 058 **se pasa**"),
    ("A697", "749", 4, "Pepe", "Jose", "RONDA 4\nJ1 - Pepe - 749 (20)\nJ2 - Jose - A697 **se pasa**"),
    ("A3674", "0K2", 5, "Pepe", "Jose", "RONDA 5\nJ1 - Pepe - 0K2 **se pasa**\nJ2 - Jose - A3674 (21)"),
    ("Q8", "25367", 5, "Pepe", "Jose", "RONDA 5\nJ1 - Pepe - 25367 **se pasa**\nJ2 - Jose - Q8 (18)"),
    ("J23", "697", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - 697 **se pasa**\nJ2 - Jose - J23 (15)"),
    ("5", "Q57", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - Q57 **se pasa**\nJ2 - Jose - 5 (5)"),
    ("KJQ", "7", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - 7 (7)\nJ2 - Jose - KJQ **se pasa**"),
    ("78Q", "59K", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - 59K **se pasa**\nJ2 - Jose - 78Q **se pasa**"),
    ("994", "Q75", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - Q75 **se pasa**\nJ2 - Jose - 994 **se pasa**"),
    ("050", "J5Q", 3, "Pepe", "Jose", "RONDA 3\nJ1 - Pepe - J5Q **se pasa**\nJ2 - Jose - 050 **se pasa**"),
    ("44563", "Q37", 5, "Pepe", "Jose", "RONDA 5\nJ1 - Pepe - Q37 (20)\nJ2 - Jose - 44563 **se pasa**"),
    ("984", "23548", 5, "Pepe", "Jose", "RONDA 5\nJ1 - Pepe - 23548 **se pasa**\nJ2 - Jose - 984 (21)")
    ]
)
def test_se_pasa_params(input_n1,input_n2,input_n3,input_n4,input_n5, expected):
    assert se_pasa(input_n1,input_n2,input_n3,input_n4,input_n5) == expected