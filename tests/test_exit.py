import pytest
from unittest.mock import patch
from io import StringIO
from main import main


def test_exit_command():
    """
    Тест проверяет, что команда exit завершает цикл программы.
    """
    user_input = "exit\n"

    with patch('builtins.input', return_value="exit"):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()


def test_exit_after_commands():
    """
    Тест проверяет, что exit работает после выполнения других команд.
    """
    inputs = ["add point 0 0", "list", "exit"]

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()):
            main()


def test_exit_ignores_empty_lines():
    """
    Тест проверяет, что пустые строки игнорируются до exit.
    """
    inputs = ["", "", "exit"]

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()):
            main()
