from mdtohtml import md_to_html
from extracttitle import extract_title
import os, shutil

def generate_file(data_path, template_path, destination_path):
    print(f"Generating page from data at: {data_path}; Using template at: {template_path}; Destination: {destination_path}")
    data = ""
    template_file = ""

    with open(data_path, "r") as file:
        data = file.read()
        
    html_file = md_to_html(data).to_html()
    title = extract_title(data)

    with open(template_path, "r") as file:
        template_file = file.read()
        template_file = template_file.replace("{{ Title }}", title)
        template_file = template_file.replace("{{ Content }}", html_file)
        file.close()
    
    with open(destination_path, "w") as file:
        file.write(template_file)
        file.close()