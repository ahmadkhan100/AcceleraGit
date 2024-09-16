from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='acceleragit',
    version='1.0.0',
    author='Ahmad Khan',
    author_email='ar5khan@uwaterloo.ca',
    description='Accelerate GitHub applications by optimizing performance.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ahmadkhan100/AcceleraGit',
    packages=find_packages(),
    install_requires=[
        'astunparse>=1.6.3',
        'rich>=10.0.0',      # For enhanced CLI output
        'requests>=2.25.1',
        'gitpython>=3.1.14',
    ],
    entry_points={
        'console_scripts': [
            'acceleragit=acceleragit.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
