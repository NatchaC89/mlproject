from setuptools import find_packages,setup

def get_requirements(file_path:str):
    pass

setup(
    name='mlproject',
    version='0.0.1',
    author='Natcha',
    author_email='nutcha.pom.2532@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)