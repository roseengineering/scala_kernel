import os
from setuptools import setup, find_packages

package = 'scala_kernel'

dirname = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(dirname, "requirements.txt")) as f:
    requirements = f.read().rstrip().split('\n')

setup(
    name=package,
    version='0.1.0',
    description='A Jupyter kernel for Scala',
    url='https://github.com/roseengineering',
    author='roseengineering',
    author_email='roseengineering@github.com',
    license='MIT',
    keywords='scala jupyter ipython development',
    packages=[package],
    install_requires=requirements
)
