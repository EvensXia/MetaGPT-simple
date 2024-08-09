import subprocess


def install_mermaid_cli():
    """Install mermaid-cli using npm."""
    try:
        subprocess.check_call(["npm", "install", "-g", "@mermaid-js/mermaid-cli"])
        print("mermaid-cli installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output}")


if __name__ == "__main__":
    install_mermaid_cli()
