from setuptools import setup

with open('README.md','r') as f:
    long_description=f.read()

setup(
        name='deep_gender_prediction_from_name',
        version='1.0',
        license='MIT',
        long_description=long_description,
        author='Steve Chiu',
        author_email='steve.scchiu@gmail.com',
        packages=['dgpn'],
        install_requires=[
            'keras==2.1.1',
            'tensorflow==1.4.1',
            'pandas',
            'sklearn'
            ],
        scripts=[]
)
