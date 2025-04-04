import os

# Define the project structure
structure = {
    "shadow-os": {
        "src": {
            "__init__.py": "",
            "vaultmind": {
                "__init__.py": "",
                "storage.py": "# VaultMind storage logic\n",
                "analysis.py": "# VaultMind analysis logic\n"
            },
            "echotwin": {
                "__init__.py": "",
                "reflection.py": "# EchoTwin reflection logic\n"
            },
            "interface": {
                "__init__.py": "",
                "console.py": "# Console interface\n"
            },
            "utils": {
                "__init__.py": "",
                "helpers.py": "# Utility functions\n"
            }
        },
        "data": {
            "vaultmind.db": ""  # Empty, will be created by app
        },
        "tests": {
            "__init__.py": "",
            "test_vaultmind.py": "# Unit tests for VaultMind\n"
        },
        "config": {
            "settings.py": "# App configuration\nDB_PATH = 'data/vaultmind.db'\n"
        },
        ".gitignore": "venv/\ndata/vaultmind.db\n__pycache__/\n*.pyc\n",
        "README.md": "# Shadow OS\nA soul operating system to reflect, evolve, and remember who you are.\n\n## Structure\n- src/: Core logic\n- data/: Storage\n- tests/: Tests\n- config/: Settings\n",
        "main.py": "# Shadow OS entry point\n"
    }
}

def create_structure(base_path, structure):
    """Recursively create directories and files from a nested dict."""
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Run the setup
if __name__ == "__main__":
    base_dir = "shadow-os"
    os.makedirs(base_dir, exist_ok=True)
    create_structure(base_dir, structure["shadow-os"])
    print(f"Created Shadow OS structure in {base_dir}/")