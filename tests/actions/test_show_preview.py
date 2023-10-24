import pytest
from pro_filer.actions.main_actions import show_preview  # NOQA

str_01 = "Found 3 files and 2 directories\n"
str_02 = "First 5 files: ['src/__init__.py',"
str_03 = " 'src/app.py', 'src/utils/__init__.py']\n"
str_04 = "First 5 directories: ['src', 'src/utils']\n"


# 01: rejeita implementações que consideram apenas all_files e all_dirs vazios
@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {"all_files": [], "all_dirs": []},
            "Found 0 files and 0 directories\n",
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            f"{str_01}{str_02}{str_03}{str_04}",
        ),
    ],
)
def test_context_vazio_e_nao_vazio(capsys, context, expected):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected


str_05 = "Found 6 files and 6 directories\n"
str_06 = "First 5 files: ['pasta_01/arquivo_01.py',"
str_07 = " 'pasta_02/arquivo_02.py', 'pasta_03/arquivo_03.py',"
str_08 = " 'pasta_04/arquivo_04.py', 'pasta_05/arquivo_05.py']\n"
str_09 = "First 5 directories: ['pasta_01', 'pasta_02',"
str_10 = " 'pasta_03', 'pasta_04', 'pasta_05']\n"


# 02: rejeita implementações que exibem mais do que 5 arquivos e/ou diretórios
@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {
                "all_files": [
                    "pasta_01/arquivo_01.py",
                    "pasta_02/arquivo_02.py",
                    "pasta_03/arquivo_03.py",
                    "pasta_04/arquivo_04.py",
                    "pasta_05/arquivo_05.py",
                    "pasta_06/arquivo_06.py",
                ],
                "all_dirs": [
                    "pasta_01",
                    "pasta_02",
                    "pasta_03",
                    "pasta_04",
                    "pasta_05",
                    "pasta_06",
                ],
            },
            f"{str_05}{str_06}{str_07}{str_08}{str_09}{str_10}",
        ),
    ],
)
def test_exibe_apenas_cinco_primeiros(capsys, context, expected):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected
