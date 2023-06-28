import setuptools


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()



VERSION = '1.0.0'
DESCRIPTION = 'Typewriter effect for python'
LONG_DESCRIPTION = long_description

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
    python_requires='>=3.7',
    py_modules=['pywriter'],
    keywords=['python', 'pywriter', 'type', 'writer', 'typewriter', 'typewritereffect'],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: Printing",
        "Topic :: Text Processing",
        "Topic :: Terminals",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        
    ]
)
