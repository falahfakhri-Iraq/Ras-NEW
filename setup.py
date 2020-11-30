import setuptools


with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name='Raster',
    version='0.0.1',
    author='Falah Fakhri',
    author_email='falah.fakhri@outlook.com',
    description='A small mathematic library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/falahfakhri-Iraq/Raster',
    packages=setuptools.find_packages(),
    classification=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',

    ],
    python_requires='>=3.6',
  )
