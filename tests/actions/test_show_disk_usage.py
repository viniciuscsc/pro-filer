from pro_filer.actions.main_actions import show_disk_usage  # NOQA

import pytest


@pytest.fixture
def arquivos_temporarios(tmp_path):
    arquivo1 = tmp_path / "arquivo1.txt"
    arquivo1.write_text("a")

    arquivo2 = tmp_path / "arquivo2.txt"
    arquivo2.write_text("aaa")

    return [str(arquivo1), str(arquivo2)]
