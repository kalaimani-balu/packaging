from setuptools import setup

setup(
    name='packaging',
    version='0.1.0',
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Kalaimani Balu',
    author_email='kalaimani.balu@gmail.com',
    license='Apache License 2.0',
    packages=['packaging'],

    entry_points={
            'console_scripts': ['exec-pkg=packaging.exec_pkg:main'],
        },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Information security',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
