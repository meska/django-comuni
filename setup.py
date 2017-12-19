from setuptools import setup
import sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

setup(
    name='django-comuni',
    version='0.2.2',
    install_requires=requirements,
    url='https://gitlab.com/meska/django-comuni',
    license='MIT',
    author='Marco Mescalchin',
    author_email='meskatech@gmail.com',
    description='Tabelle Comuni Italiani per Django',
    packages=['comuni'],
    package_dir={'comuni': 'comuni'},
    package_data={
        'comuni': [
            'migrations/*.*',
            'migrations/fixtures/*.*'
        ]}

)
