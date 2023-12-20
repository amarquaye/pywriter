# Pywriter

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Badge](https://img.shields.io/badge/python-3.x-color.svg)](#)
[![PyPI](https://img.shields.io/pypi/v/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![Downloads](https://static.pepy.tech/badge/pywriter)](https://pepy.tech/project/pywriter)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/amarquaye/pywriter)

Pywriter is a Python module for printing text to your console or terminal in the classic typewriter effect.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pywriter.

```bash
pip install pywriter
```


## Usage

```python
import pywriter

# returns 'Hello World!' character by character at the rate of one character per second
pywriter.write('Hello World!', rate=1)

# Let's introduce my latest features
pywriter.writer('Hello World!', rate=1)
pywriter.typewriter('Hello World!', new="Jesse", idx=6, rate=1)



# You can decide to exclude the rate argument.
# That will print out your text at the default rate of 0.1


```

## Alternate Usage
```python
from pywriter import write, writer, typewriter

# returns 'Hello World!' character by character at the rate of one character per second
write('Hello World!', rate=1)

# Let's introduce my latest features
writer('Hello World!', rate=1)
typewriter('Hello World!', new="Jesse", idx=6, rate=1)


# However, it is recommended that you use pywriter.write
#instead of using the write function directly.
# Since this will help prevent any conflict in case there
#is another python module which also has a write function.

```
<br/>

## Demo

![ui_glow_up](https://user-images.githubusercontent.com/96346994/233510322-9397b5b3-8626-447a-9453-0e580beae656.gif)

<br/>

## Changelog

### v1.0.0 (29/06/2023)

### Feature

- First major update of `pywriter`
- Added function to print output with typewriter effect in reverse.
  The name of this new function is ```writer```.
- Also added function to print output with typewriter effect.
  In a way that it deletes some part of the text to some index and prints another text to replace the previous text.
  And name of my most recent and favourite function is ```typewwriter```.


### v0.1.1 (21/04/2023)

### Feature

- First minor update of `pywriter`
- Added compatibility with terminal and any console.

### Fix

- Fixed issue with windows cmd waiting for the entire program to run before output in seen.


### v0.0.1 (15/04/2023)

- First release of `pywriter`

<br/>

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[AGPL v3.0](https://github.com/amarquaye/pywriter/blob/master/LICENSE)


## Authors

- [Jesse Amarquaye](https://www.github.com/amarquaye)


## Roadmap

- Add more integrations.

<br/>

## About Me

- 👨‍💻 All of my projects are available at [https://www.github.com/amarquaye](https://www.github.com/amarquaye)

- 📫 How to reach me via mail **jesseamarquayelegendary@gmail.com**

<h2 align="left">Connect with me:</h2>
<p align="left">
<a href="https://twitter.com/llordjesse" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="llordjesse" height="30" width="40" /></a>
<a href="https://linkedin.com/in/amarquaye" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="amarquaye" height="30" width="40" /></a>
<a href="https://fb.com/llordjesse" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="llordjesse" height="30" width="40" /></a>
<a href="https://instagram.com/llordjesse" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="llordjesse" height="30" width="40" /></a>
</p>


## Feedback

If you have any feedback, please reach out to us at jesseamarquayelegendary@gmail.com
