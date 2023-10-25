from pro_filer.actions.main_actions import show_disk_usage  # NOQA


# 01: verificar a saida do diretorio vazio
def test_espaco_usado_diretorio_vazio(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    espaco_usado = captured.out

    assert "Total size: 0" in espaco_usado
