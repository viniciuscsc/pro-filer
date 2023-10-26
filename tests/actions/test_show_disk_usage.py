from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest


# 01: verificar a saida do diretorio vazio
@pytest.mark.parametrize(
        "context, expected",
        [
            (
                {"all_files": []},
                "Total size: 0",
            ),
        ],
)
def test_espaco_usado_diretorio_vazio(capsys, context, expected):
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == expected
