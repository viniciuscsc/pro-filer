from pro_filer.actions.main_actions import show_disk_usage  # NOQA

import pytest
import os
from unittest.mock import patch


@pytest.fixture
def arquivos_temporarios(tmp_path):
    arquivo1 = tmp_path / "arquivo1.txt"
    arquivo1.write_text("a")

    arquivo2 = tmp_path / "arquivo2.txt"
    arquivo2.write_text("aaa")

    return [str(arquivo1), str(arquivo2)]


def mockar_funcao_get_printable_file_path(caminho_arquivo):
    return caminho_arquivo


def test_espaco_usado_com_arquivos(capsys, arquivos_temporarios):
    context = {"all_files": arquivos_temporarios}

    tamanho_total = sum(
        os.path.getsize(arquivo) for arquivo in arquivos_temporarios
    )

    arquivos_ordenados = sorted(
        context["all_files"], key=os.path.getsize, reverse=True
    )

    saida_esperada = []

    for arquivo in arquivos_ordenados:
        tamanho_arquivo = os.path.getsize(arquivo)
        caminho_formatado = mockar_funcao_get_printable_file_path(
            arquivo
        ).ljust(70)
        percentual = int(tamanho_arquivo / tamanho_total * 100)
        saida_esperada.append(
            f"'{caminho_formatado}': {tamanho_arquivo} ({percentual}%)"
        )

    saida_esperada.append(f"Total size: {tamanho_total}")

    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path",
        side_effect=mockar_funcao_get_printable_file_path,
    ):
        show_disk_usage(context)
        captured = capsys.readouterr()
        saida_real = captured.out.splitlines()

    assert saida_real == saida_esperada


def test_espaco_usado_sem_arquivos(capsys):
    context = {"all_files": []}

    saida_esperada = ["Total size: 0"]

    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path",
        side_effect=mockar_funcao_get_printable_file_path,
    ):
        show_disk_usage(context)
        captured = capsys.readouterr()
        saida_real = captured.out.splitlines()

    assert saida_real == saida_esperada
