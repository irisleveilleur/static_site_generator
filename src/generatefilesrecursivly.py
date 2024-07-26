from generatefile import generate_file
import os

def generate_files_recursivly(content_path, template_path, destination_path):
    to_generate = os.listdir(content_path)

    for i in to_generate:
        if os.path.isfile(f"{content_path}/{i}"):
            generate_file(f"{content_path}/{i}", template_path, f"{content_path.replace("content", destination_path)}/{i.replace("md", "html")}")
        else:
            os.mkdir(f"{content_path.replace("content", destination_path)}/{i}")
            generate_files_recursivly(f"{content_path}/{i}", template_path, destination_path)