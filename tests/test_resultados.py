import pytest
from src.blackjat import resultado_texto

@pytest.mark.parametrize(
    "input_n1,input_n2,input_n3,input_n4,input_n5,expected",
    [
    ("A5", "Q5", 2, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  2\n¡Empate!\nJ1 - Pepe - Q5 (15)\nJ2 - Jose - A5 (15)"),
    ("A59", "Q57", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\n¡Gana J2 - Jose!\nJ1 - Pepe - Q57 (22)\nJ2 - Jose - A59 (15)"),
    ("4563", "Q0", 4, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  4\n¡Gana J1 - Pepe!\nJ1 - Pepe - Q0 (20)\nJ2 - Jose - 4563 (18)"),
    ("058", "J49", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\nGame over ¡Los dos os habéis pasado!\nJ1 - Pepe - J49 (23)\nJ2 - Jose - 058 (23)"),
    ("A697", "749", 4, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  4\n¡Gana J1 - Pepe!\nJ1 - Pepe - 749 (20)\nJ2 - Jose - A697 (23)"),
    ("A3674", "0K", 5, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  5\n¡Gana J2 - Jose!\nJ1 - Pepe - 0K (20)\nJ2 - Jose - A3674 (21)"),
    ("Q8", "25362", 5, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  5\n¡Empate!\nJ1 - Pepe - 25362 (18)\nJ2 - Jose - Q8 (18)"),
    ("J23", "69", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\n¡Empate!\nJ1 - Pepe - 69 (15)\nJ2 - Jose - J23 (15)"),
    ("5", "Q57", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\n¡Gana J2 - Jose!\nJ1 - Pepe - Q57 (22)\nJ2 - Jose - 5 (5)"),
    ("KJQ", "7", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\n¡Gana J1 - Pepe!\nJ1 - Pepe - 7 (7)\nJ2 - Jose - KJQ (30)"),
    ("78Q", "59K", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\nGame over ¡Los dos os habéis pasado!\nJ1 - Pepe - 59K (24)\nJ2 - Jose - 78Q (25)"),
    ("99", "Q7", 2, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  2\n¡Gana J2 - Jose!\nJ1 - Pepe - Q7 (17)\nJ2 - Jose - 99 (18)"),
    ("050", "J5Q", 3, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  3\nGame over ¡Los dos os habéis pasado!\nJ1 - Pepe - J5Q (25)\nJ2 - Jose - 050 (25)"),
    ("4457A", "Q37", 5, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  5\n¡Gana J2 - Jose!\nJ1 - Pepe - Q37 (20)\nJ2 - Jose - 4457A (21)"),
    ("982", "23546", 5, "Pepe", "Jose", "JUEGO TERMINADO - Ronda  5\n¡Gana J1 - Pepe!\nJ1 - Pepe - 23546 (20)\nJ2 - Jose - 982 (19)")
    ]
)
def test_resultado_texto_params(input_n1,input_n2,input_n3,input_n4,input_n5, expected):
    assert resultado_texto(input_n1,input_n2,input_n3,input_n4,input_n5) == expected