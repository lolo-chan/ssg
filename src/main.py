import os
import shutil

def static_to_public(source: str, dest: str):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for i in os.listdir(source):
        if os.path.isfile(os.path.join(os.getcwd(), source, i)):
            shutil.copy(f"{source}/{i}", dest)
            print(f"copied {i} to {dest}/")
        elif os.path.isdir(os.path.join(os.getcwd(), source, i)):
            print(f"copied {i}/ to {dest}/")
            static_to_public(f"{source}/{i}", f"{dest}/{i}")


def main():
    static_to_public("static", "public")


main()