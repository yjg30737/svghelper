import os
import xml.etree.ElementTree as ET


def set_color(input_file: str, output_file: str, replace_color: str):
    tree = ET.parse(input_file)
    root = tree.getroot()
    for el in root.iter():
        name = el.tag.split('}')[1]
        if name == 'path':
            el.set('fill', replace_color)
    with open(output_file, 'wb') as f:
        tree.write(f)

def set_color_to_files(input_dir: str, output_dir: str, replace_color: str):
    filenames = [os.path.join(os.path.abspath(input_dir), filename)
                 for filename in os.listdir(input_dir)]

    for filename in filenames:
        set_color(filename, os.path.join(os.path.join(os.getcwd(), output_dir),
                                         os.path.basename(filename)), replace_color)