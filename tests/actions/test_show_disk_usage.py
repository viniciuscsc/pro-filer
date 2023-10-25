from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import patch


# 01: verificar a saida do diretorio vazio
def test_espaco_usado_diretorio_vazio(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    espaco_usado = captured.out

    assert "Total size: 0" in espaco_usado


# 02: verificar o espaco usado e tamanho dos arquivos
def test_espaco_usado(capsys, context, tmp_path):
    arquivo_01 = tmp_path / "arquivo_01.txt"
    arquivo_01.write_text("Conteudo do arquivo 01")

    arquivo_02 = tmp_path / "arquivo_2.txt"
    arquivo_02.write_text("Conteudo do arquivo 02")

    context = {
        "all_files": [
            str(arquivo_01),
            str(arquivo_02),
        ]
    }

    with patch(
        "pro_filer.cli_helpers._get_printable_file_path"
    ) as funcao_substituta:
        funcao_substituta.return_value = "mock_caminho_arquivo"

        show_disk_usage(context)
        captured = capsys.readouterr()
        saida_espaco_usado = captured.out

        # arquivos estao corretos
        assert "'mock_caminho_arquivo'" in saida_espaco_usado
        assert "Conteudo do arquivo 01" in saida_espaco_usado
        assert "Conteudo do arquivo 02" in saida_espaco_usado

        # tamanho total esta correto
        assert "Total size: 44" in saida_espaco_usado
