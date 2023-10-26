from pro_filer.actions.main_actions import show_details  # NOQA

import pytest
from datetime import date

data_atual = date.today()
data_formatada = data_atual.strftime("%Y-%m-%d")

str_1 = "File name: arquivo_teste.txt\n"
str_2 = "File size in bytes: 0\n"
str_3 = "File type: file\n"
str_4 = "File extension: .txt\n"
str_5 = f"Last modified date: {data_formatada}\n"

str_6 = "File extension: [no extension]\n"


# 01: exibe as mensagens corretas
@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {"base_path": "arquivo_teste.txt"},
            f"{str_1}{str_2}{str_3}{str_4}{str_5}",
        ),
    ],
)
def test_exibe_mensagem_correta(capsys, context, expected):
    with open("arquivo_teste.txt", "w"):
        pass
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected


# 02: usa o formato de data correto
def test_exibe_data_formato_correto(capsys):
    context = {"base_path": "arquivo_teste.txt"}

    with open("arquivo_teste.txt", "w"):
        pass
    show_details(context)
    captured = capsys.readouterr()

    linha_info_data = captured.out.splitlines()[-1].strip()

    assert linha_info_data == f"Last modified date: {data_formatada}"


# 03: arquivo não existente
@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {"base_path": "arquivo_nao_existente.txt"},
            "File 'arquivo_nao_existente.txt' does not exist\n",
        ),
    ],
)
def test_arquivo_nao_existente(capsys, context, expected):
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected


# 04: arquivo sem extensão
@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {"base_path": "arquivo_teste"},
            f"{str_1}{str_2}{str_3}{str_6}{str_5}",
        ),
    ],
)
def test_arquivo_sem_extensao(capsys, context, expected):
    with open("arquivo_teste", "w"):
        pass
    show_details(context)
    captured = capsys.readouterr()
    assert "File extension: [no extension]" in captured.out
