from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file.obj.readlines()
        requirements=[req.replace("\n,","") for req in requirements]
    return requirements


setup(
    name='Sensors Fault Detection',
    version='0.0.1',
    author='Shubham',
    author_mail='sv.shubham004@gmail.com',
    install_requirements=('requirements.txt'),
    packages=find_packages()
)