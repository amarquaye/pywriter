# Pywriter

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Badge](https://img.shields.io/badge/python-3.x-color.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/pywriter.svg)](https://pypi.org/project/pywriter/)
[![Downloads](https://static.pepy.tech/badge/pywriter)](https://pepy.tech/project/pywriter)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/amarquaye/pywriter)

Pywriter is a Python module for printing text to your console or terminal in the classic _typewriter effect_.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pywriter.

```bash
pip install pywriter
```

## Usage

```python
import pywriter as pw


# returns 'Hello World!' character by character at the rate of one character per second
pw.write('Hello World!', rate=1)

# Let's introduce my latest features
pw.reverse('Hello World!', rate=1)
pw.typewriter('Hello World!', new="Jesse", idx=6, rate=1)



# You can decide to exclude the rate argument.
# That will print out your text at the default rate of 0.01

```

## Alternate Usage

```python
from pywriter import write, reverse, typewriter


# returns 'Hello World!' character by character at the rate of one character per second
write('Hello World!', rate=1)

# Let's introduce my latest features
reverse('Hello World!', rate=1)
typewriter('Hello World!', new="Jesse", idx=6, rate=1)


# However, it is recommended that you use pywriter.write
#instead of using the write function directly.
# Since this will help prevent any conflict in case there
#is another python module which also has a write function.

```

## Demo

![ui_glow_up](https://user-images.githubusercontent.com/96346994/233510322-9397b5b3-8626-447a-9453-0e580beae656.gif)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

- [MIT](https://github.com/amarquaye/pywriter/blob/master/LICENSE)

## Authors

- [Jesse Amarquaye](https://www.github.com/amarquaye).

## Roadmap

- Adding more features soon.

## About Me

- 👨‍💻 All of my projects are available at [https://www.github.com/amarquaye](https://www.github.com/amarquaye).

- 📫 You can [reach me via mail](mailto:engineeramarquaye@gmail.com).

<h2 align="left">Connect with me:</h2>
<p align="left">
<a href="https://linkedin.com/in/amarquaye" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Connect on linkedin" height="30" width="40" /></a>
<a href="https://www.reddit.com/user/amarquaye/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/reddit.svg" alt="Connect on reddit" height="30" width="40" /></a>

## Feedback

If you have any feedback, please [reach out to me](mailto:engineeramarquaye@gmail.com).

## Disclaimer

Pywriter is provided as-is and does not require frequent updates. While it remains functional and usable, future updates will be made only if necessary. If you find the project useful but notice a lack of recent activity, this **does not mean it is abandoned**. Contributions are welcome via pull requests.
