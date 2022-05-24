import os
import xml.etree.ElementTree as ET

from colorgetter import *


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

def set_comp_color(input_file: str, output_file: str):
    tree = ET.parse(input_file)
    root = tree.getroot()
    for el in root.iter():
        name = el.tag.split('}')[1]
        if name == 'path':
            color = el.get('fill', '#000000')
            comp_color = rgb_to_hex(
                            *get_complementary_color(
                                *hex_to_rgb(color)
                            )
                        )
            el.set('fill', comp_color)
    with open(output_file, 'wb') as f:
        tree.write(f)

def set_files_comp_color(input_dir: str, output_dir: str):
    filenames = [os.path.join(os.path.abspath(input_dir), filename)
                 for filename in os.listdir(input_dir)]

    for filename in filenames:
        set_comp_color(filename, os.path.join(os.path.join(os.getcwd(), output_dir),
                                             os.path.basename(filename)))