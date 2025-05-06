from setuptools import find_packages, setup # type: ignore
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of packages from the given requirements file,
    excluding the editable install line if present.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='machinelearningproject',
    version='0.0.1',
    author='vinodh',
    author_email='svinodhkumar961@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
