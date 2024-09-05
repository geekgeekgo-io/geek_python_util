from setuptools import setup, find_packages

setup(
    name='geek_python_util',
    version='1.0.6',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='A reusable geek util for Python applications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='GeekGeekGo',
    author_email='geekgeekgo@gmail.com',
    url='https://github.com/geekgeekgo-io/geek_python_util',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
