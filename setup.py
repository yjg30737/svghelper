from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='svghelper',
    version='0.0.6',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Python SVG helper. set svg color, etc.',
    url='https://github.com/yjg30737/svghelper.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'colorgetter>=0.0.1'
    ]
)