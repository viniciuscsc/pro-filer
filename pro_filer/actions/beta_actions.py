"""Arquivo que estudantes devem editar"""


def calcular_profundidade_diretorio(caminho: str):
    return caminho.count("/")


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        profundidade = calcular_profundidade_diretorio
        deepest_file = max(context["all_files"], key=profundidade)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name = file_name.lower()
            search_term = search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
