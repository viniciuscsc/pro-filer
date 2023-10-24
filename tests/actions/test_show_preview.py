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
