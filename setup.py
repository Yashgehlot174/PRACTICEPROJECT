from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, encoding='utf-8') as file_obj:
        for line in file_obj:
            req = line.strip()
            if not req or req.startswith('#'):
                continue
            if req == HYPEN_E_DOT:
                continue
            requirements.append(req)
    return requirements

setup(
    name="PRACTICEPROJECT",
    version="0.0.1",
    author="Yash",
    author_email="yash_g@ece.iitr.ac.in",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)