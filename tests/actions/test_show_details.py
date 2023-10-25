from pro_filer.actions.main_actions import show_details  # NOQA

import pytest

str_1 = "File name: arquivo_teste.txt\n"
str_2 = "File size in bytes: 0\n"
str_3 = "File type: file\n"
str_4 = "File extension: .txt\n"
str_5 = "Last modified date: 2023-10-25\n"


# 01: exibe as mensagens corretas
@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {"base_path": "arquivo_teste.txt"},
            f"{str_1}{str_2}{str_3}{str_4}{str_5}",
        )
    ],
)
def test_exibe_mensagem_correta(capsys, context, expected):
    with open("arquivo_teste.txt", "w"):
        pass
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected
