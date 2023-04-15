import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Typewriter effect for python'
LONG_DESCRIPTION = 'A package that allows you to print text in your termimal in the classic typewriter style.'

# Setting up
setuptools.setup(
    name="pywriter",
    version=VERSION,
    author="Jesse Amarquaye",
    author_email="jesseamarquayelegendary@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    include_package_data=True,
    url= "https://github.com/amarquaye/pywriter",
    # install_requires=['time'],
    python_requires='>=3.7',
    py_modules=['pywriter'],
    keywords=['python', 'pywriter', 'writer', 'typewriter', 'typewritereffect'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        
    ]
)