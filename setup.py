from setuptools import setup, find_packages

setup(
    name='onedrivemirror',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    author='w',
    author_email='',
    description='',
    install_requires='onedrivesdk',
    entry_points= {
            'console_scripts': ['onedrivemirror = onedrivemirror.__main__:main'],
    }
)
