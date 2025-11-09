import yaml

def load_author_info(path="configs/author.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)

def print_framework_header():
    author_info = load_author_info()["author"]
    print("\n============================================================")
    print(f"Author:  {author_info['name']}  —  {author_info['role']}")
    print(f"Website: {author_info['website']}")
    print(f"Email:   {author_info['email']}")
    print("============================================================\n")
