from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will retun the list of requiremnts
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML_AWS',
    version='0.0.1',
    author='Nikhil',
    author_email='nikhil.kum.828283@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')
)