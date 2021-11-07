import os


def new_dir(dir_name):
    try:
        new_path = os.path.join(os.environ.get("RESEARCH_PATH"), dir_name)
        os.makedirs(new_path)
        print("A directory is created at path -", new_path)
    except OSError as e:
        print(e)


if __name__ == "__main__":
    new_dir("sample_dir_name")
