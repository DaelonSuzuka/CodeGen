from distutils.core import setup

setup(
    name='CodeGen',
    version='0.1dev',
    author='David Kincaid',
    author_email='dlkincaid0@gmail.com',
    packages=['codegen',],
    install_requires=['dotmap',],
    license='MIT',
    long_description=open('README.md').read(),
)