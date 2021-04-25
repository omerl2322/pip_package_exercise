from setuptools import setup

setup(
    name='universities_exercise_api',
    version='0.0.1',
    description='A simple api for working with universities data',
    py_modules=['universities_api'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'License:: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=['requests>=2.25.1']
    
)