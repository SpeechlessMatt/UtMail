import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='utmail',
      version='0.1.5',
      description='Offer a uniform interface for free temp mail.',
      long_description=long_description,    #包的详细介绍，一般在README.md文件内
      long_description_content_type="text/markdown",
      url='https://github.com/SpeechlessMatt/UtMail',
      author='Czy_4201b',
      author_email='speechlessmatt@qq.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      install_requires=[
          "loguru>=0.7.2",
          "requests>=2.32.3"
      ],
      zip_safe=False)