import os

def create_project_structure(base_dir):
    # Diretórios principais e subdiretórios
    structure = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src/data_processing",
        "src/models",
        "src/evaluation",
        "src/visualization",
        "tests",
        "outputs",
        "docs"
    ]

    # Criar os diretórios
    for folder in structure:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Criado: {path}")

    # Criar arquivos principais
    files = [
        "README.md",
        ".gitignore",
        "requirements.txt",
        "config.yaml"
    ]

    for file in files:
        file_path = os.path.join(base_dir, file)
        with open(file_path, "w") as f:
            f.write("")  # Cria um arquivo vazio
        print(f"Criado: {file_path}")

# Caminho base do projeto
base_directory = input("Digite o nome do diretório base do projeto: ")
os.makedirs(base_directory, exist_ok=True)
create_project_structure(base_directory)
print("Estrutura criada com sucesso!")
