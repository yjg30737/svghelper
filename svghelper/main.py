import os
import xml.etree.ElementTree as ET


def set_color(input_file: str, output_file: str, output_color: str):
    tree = ET.parse(input_file)
    root = tree.getroot()
    for el in root.iter():
        name = el.tag.split('}')[1]
        if name == 'path':
            el.set('fill', output_color)
    with open(output_file, 'wb') as f:
        tree.write(f)

def set_files_color(input_dir: str, output_dir: str, output_color: str):
    filenames = [os.path.join(os.path.abspath(input_dir), filename)
                 for filename in os.listdir(input_dir)]

    for filename in filenames:
        set_color(filename, os.path.join(os.path.join(os.getcwd(), output_dir),
                                         os.path.basename(filename)), output_color)

def replace_color(input_file: str, output_file: str, input_color: str, output_color: str):
    tree = ET.parse(input_file)
    root = tree.getroot()
    for el in root.iter():
        name = el.tag.split('}')[1]
        if name == 'path':
            if el.get('fill', input_color) == input_color:
                el.set('fill', output_color)
    with open(output_file, 'wb') as f:
        tree.write(f)

def replace_files_color(input_dir: str, output_dir: str, input_color: str, output_color: str):
    filenames = [os.path.join(os.path.abspath(input_dir), filename)
                 for filename in os.listdir(input_dir)]

    for filename in filenames:
        replace_color(filename, os.path.join(os.path.join(os.getcwd(), output_dir),
                                             os.path.basename(filename)), input_color, output_color)