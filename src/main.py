import shutil, os
from generatefilesrecursivly import generate_files_recursivly

def copy_file(path):
    to_copy = os.listdir(path)

    for i in to_copy:
        if os.path.isfile(f"{path}/{i}"):
            shutil.copy(f"{path}/{i}", f"{path.replace("static", "public")}/{i}")
        else:
            os.mkdir(f"{path.replace("static", "public")}/{i}")
            copy_file(f"{path}/{i}")

        

def main():
    if os.path.exists("public/"):
        shutil.rmtree("public/")
    os.mkdir("public")
    copy_file("static")
    generate_files_recursivly("content", "template.html", "public")
    

if __name__ == "__main__":
    main()