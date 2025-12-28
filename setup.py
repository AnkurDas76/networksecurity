from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements..
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines ans -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    
    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ankur Das",
    author_email="ankurdas7602@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)
              