from setuptools import find_packages, setup # type: ignore
from typing import List


e_dot = '-e .'
def get_requirements(file_path: str)->list[str]:
    '''
    This function will return a list of requirements

    '''
    requirements =[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]


        if e_dot in requirements:
            requirements.remove(e_dot)
    return requirements



setup(
name='end-to-end ML project',
version='0.0.1',
author='TejaswiSaiKumar',
author_email='parepallitejaswi15@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)